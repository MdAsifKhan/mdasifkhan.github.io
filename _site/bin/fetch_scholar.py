#!/usr/bin/env python3
"""
Fetches publications from Google Scholar and regenerates `_bibliography/papers.bib`.

The script scrapes the public profile (no login required), parses the
publication list, and produces lightweight BibTeX entries that work with
jekyll-scholar. Intended for quick refreshes of the academic website.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from http.cookiejar import CookieJar
from pathlib import Path
from typing import Dict, Iterable, List, Tuple
from urllib.parse import parse_qs, urlencode, urljoin, urlparse
from urllib.request import HTTPCookieProcessor, Request, build_opener

from bs4 import BeautifulSoup

SCHOLAR_BASE = "https://scholar.google.com"
PROFILE_ID = "Akp4gEwAAAAJ"
ROWS_PER_PAGE = 20
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


@dataclass
class Publication:
    key: str
    title: str
    authors: List[str]
    venue: str
    year: str
    entry_type: str
    extra_fields: Dict[str, str]


def main() -> None:
    html_pages = list(iter_pages())
    if not html_pages:
        sys.stderr.write("No pages returned from Google Scholar.\n")
        sys.exit(1)

    publications: List[Publication] = []
    for html in html_pages:
        publications.extend(parse_page(html))

    if not publications:
        sys.stderr.write("Did not find any publications in the scraped pages.\n")
        sys.exit(1)

    publications.sort(key=lambda pub: pub.year, reverse=True)
    write_bibtex(publications)
    print(f"Updated _bibliography/papers.bib with {len(publications)} entries.")


def iter_pages() -> Iterable[str]:
    """Yield successive pages of the Scholar profile until no results remain."""
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    common_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": SCHOLAR_BASE,
    }

    for start in range(0, 400, ROWS_PER_PAGE):
        params = {
            "hl": "en",
            "user": PROFILE_ID,
            "view_op": "list_works",
            "sortby": "pubdate",
            "cstart": str(start),
            "pagesize": str(ROWS_PER_PAGE),
        }
        url = f"{SCHOLAR_BASE}/citations?{urlencode(params)}"
        request = Request(url, headers=common_headers)
        with opener.open(request) as response:
            html = response.read().decode("utf-8")

        if "There are no articles in this profile." in html:
            if start == 0:
                # This indicates a failed scrape (blocked or incorrect profile id).
                sys.stderr.write("Profile returned no articles; check connectivity or PROFILE_ID.\n")
            break

        yield html

        # If the page returned fewer rows than requested, we've reached the end.
        if count_rows(html) < ROWS_PER_PAGE:
            break


def count_rows(html: str) -> int:
    soup = BeautifulSoup(html, "html.parser")
    rows = [
        row
        for row in soup.select("tr.gsc_a_tr")
        if "gsc_a_e" not in row.get("class", [])
    ]
    return len(rows)


def parse_page(html: str) -> List[Publication]:
    soup = BeautifulSoup(html, "html.parser")
    publications: List[Publication] = []

    for row in soup.select("tr.gsc_a_tr"):
        if "gsc_a_e" in row.get("class", []):
            # Message row such as "There are no articles ..."
            continue

        link = row.select_one("a.gsc_a_at")
        if not link:
            continue

        title = clean_text(link.get_text(" ", strip=True))
        citation_key = extract_citation_key(link.get("href", ""))
        author_text, venue_text = extract_metadata(row)
        authors = format_authors(author_text)
        year = extract_year(row, venue_text)
        entry_type, extra_fields = classify_entry(venue_text)

        publications.append(
            Publication(
                key=citation_key,
                title=title,
                authors=authors,
                venue=venue_text,
                year=year,
                entry_type=entry_type,
                extra_fields=extra_fields,
            )
        )

    return publications


def extract_citation_key(href: str) -> str:
    parsed = urlparse(urljoin(SCHOLAR_BASE, href))
    query = parse_qs(parsed.query)
    raw_key = query.get("citation_for_view", [""])[0]
    suffix = raw_key.split(":")[-1] or "entry"
    return f"scholar-{suffix}"


def extract_metadata(row) -> Tuple[str, str]:
    details = row.select("div.gs_gray")
    authors = details[0].get_text(" ", strip=True) if len(details) > 0 else ""
    venue = details[1].get_text(" ", strip=True) if len(details) > 1 else ""
    return authors, venue


def format_authors(authors_text: str) -> List[str]:
    authors_text = authors_text.replace("…", "...").replace("*", "")
    parts = [part.strip() for part in authors_text.split(",") if part.strip()]
    formatted: List[str] = []

    for part in parts:
        if part in {"...", "…"}:
            formatted.append("others")
            continue
        chunks = part.split()
        if len(chunks) >= 2:
            family = chunks[-1]
            given = " ".join(chunks[:-1])
            formatted.append(f"{family}, {given}")
        else:
            formatted.append(part)

    return formatted or ["others"]


def extract_year(row, fallback: str) -> str:
    year_node = row.select_one("td.gsc_a_y span")
    if year_node and year_node.get_text(strip=True):
        return year_node.get_text(strip=True)

    match = re.search(r"(19|20)\d{2}", fallback)
    return match.group(0) if match else ""


def classify_entry(venue_text: str) -> Tuple[str, Dict[str, str]]:
    venue_text = clean_text(venue_text)
    lower = venue_text.lower()

    if not venue_text:
        return "misc", {}

    conference_keywords = [
        "conference",
        "proceedings",
        "neurips",
        "icml",
        "aistats",
        "iclr",
        "cvpr",
        "nips",
        "acm",
        "ieee",
    ]
    if "arxiv" in lower or "medrxiv" in lower or "bioarxiv" in lower:
        return "misc", {"howpublished": venue_text}
    if any(keyword in lower for keyword in conference_keywords):
        return "inproceedings", {"booktitle": venue_text}
    return "article", {"journal": venue_text}


def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = text.replace(" , ", ", ")
    text = re.sub(r", (19|20)\d{2}$", "", text)
    text = re.sub(r"\.\s+(?=\d)", ".", text)
    return text


def bib_escape(value: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def write_bibtex(publications: Iterable[Publication]) -> None:
    lines = ["---", "---", ""]
    for pub in publications:
        lines.append(f"@{pub.entry_type}{{{pub.key},")
        lines.append(f"  title = {{{bib_escape(pub.title)}}},")
        if pub.authors:
            author_value = " and ".join(pub.authors)
            lines.append(f"  author = {{{bib_escape(author_value)}}},")
        if pub.year:
            lines.append(f"  year = {{{pub.year}}},")

        for field, value in pub.extra_fields.items():
            if value:
                lines.append(f"  {field} = {{{bib_escape(value)}}},")

        lines.append("}")
        lines.append("")

    output_path = Path("_bibliography/papers.bib")
    output_path.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
