### OOTechnologies – Python Web Scraping Assessment

Welcome to the **Web Scraping & Automation Intern** assessment.  
Your task is to build a Python script that scrapes data from [https://books.toscrape.com](https://books.toscrape.com)  
and saves it in a structured JSON file.


## 🎯 Task
Scrape the **latest 20 products** and export them to `data/books.json`.

Each product must include:
- `title`
- `price`
- `availability`
- `rating`
- `product_url`

Use **Python 3** with:
- `requests`
- `beautifulsoup4`
- Standard libraries (`json`, `time`, `random`, `re`, `urllib.parse`)


## ⚙️ Rules
- Implement your code in `src/scraper.py`
- Handle pagination automatically
- Add polite scraping practices:
  - Custom headers (`User-Agent`)
  - Small random delay between requests
- Save valid JSON data


## 📝 Submission

1. Fork this repo
2. Add your code in `src/scraper.py`
3. Push to your repo
4. Submit your repo link


Good luck! 

