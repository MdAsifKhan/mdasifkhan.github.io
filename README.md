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

## Configure contact form

The contact form posts to FormSubmit and forwards messages to `asif.khan@hms.harvard.edu`. On first use FormSubmit will send a verification email to activate the endpoint; approve it so future submissions arrive normally.
# mdasifkhan.github.io
