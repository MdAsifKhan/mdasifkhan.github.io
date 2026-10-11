# Asif Khan — Academic Website

This repository contains the Jekyll source for my personal academic site. Pages are written in Markdown and styled with a custom dark theme.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

## Update publications

```bash
python3 bin/fetch_scholar.py
```

The publication helper depends on BeautifulSoup:

```bash
pip install -r requirements.txt
```

## Selected publication figures

The homepage selection, topic tags, and figure metadata are defined in `selected_work` in `_config.yml`. Conceptual figures retain their aspect ratios and are displayed without links.

- `genehr-overview.svg` presents the top overview from [GenEHR Figure 1](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v2.full#F1). Its SVG viewport selects the overview from the embedded original image; the diagram is unchanged.
- `cancer-graphical-abstract.jpg` is the graphical abstract from [the Cell Reports Medicine paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12490214/), reproduced under the article's CC BY license.
- `genehr-clinical-framework.jpg` is [GenEHR Figure 7](https://www.medrxiv.org/content/10.64898/2026.09.09.26362676v2.full#F7). It illustrates the three-stage framework discussed in [the position paper](https://openreview.net/forum?id=7PJYSePp2L).

Paper-page previews below the topic tags link to the corresponding publication. Their curl and shadow are applied in CSS; the source pages are unchanged.

- `genehr-paper-preview.png` renders page 1 of [the GenEHR PDF](https://www.medrxiv.org/content/medrxiv/early/2026/09/19/2026.09.09.26362676.full.pdf).
- `pancreatic-paper-preview.png` renders page 2, the opening article page after the graphical abstract, of [the published Cell Reports Medicine PDF](https://pmc-oa-opendata.s3.amazonaws.com/PMC12490214.1/PMC12490214.1.pdf), under CC BY. Source: NIH NLM NCBI PubMed Central (PMC) Article Datasets, accessed October 8, 2026 via [the AWS dataset](https://registry.opendata.aws/ncbi-pmc/).
- `position-paper-preview.png` renders page 1 of the author-supplied `early_detection_position.pdf`, corresponding to [the position paper on OpenReview](https://openreview.net/forum?id=7PJYSePp2L).

# mdasifkhan.github.io
