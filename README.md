# OOTechnologies — Python Web Scraping Assessment

**Stack:** Python only (requests + BeautifulSoup).  
**Goal:** Scrape the latest **20 products** from https://books.toscrape.com and save to `data/books.json`.

## How to run locally
```bash
pip install -r requirements.txt
pytest -q
```

## What to edit
- Implement your logic in `src/scraper.py`
- Output must be written to `data/books.json`

## CI
Pushing to your fork will run GitHub Actions (free) and show ✅/❌ in the **Actions** tab.
