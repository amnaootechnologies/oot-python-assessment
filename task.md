# 🧠 OOTechnologies – Web Scraping & Automation Assessment

## Goal
Use **Python** (requests + BeautifulSoup) to scrape the latest **20 products**
from [https://books.toscrape.com](https://books.toscrape.com)
and export the results to `data/books.json`.

## Fields Required
| Field | Type | Example |
|-------|------|---------|
| title | string | "The Grand Design" |
| price | string | "£51.77" |
| availability | string | "In stock (22 available)" |
| rating | string | "Three" |
| product_url | string | "https://books.toscrape.com/catalogue/the-grand-design_405/index.html" |

## Rules
- Follow polite scraping: headers, small delay between requests.
- Handle pagination automatically.
- Use only: `requests`, `beautifulsoup4`, `json`, `time`, `random`, `re`, `urllib.parse`.
- Save as UTF-8 JSON file (array of at least 20 items).

## Deliverables
1. Complete your code in `src/scraper.py`.
2. Write output to `data/books.json`.
3. Commit and push to your own repo (fork).
4. Verify tests pass (GitHub Actions → green check ✅).

## Bonus (optional)
- Retry logic for failed requests.
- Respect rate limits.
- Clean and commented code.
