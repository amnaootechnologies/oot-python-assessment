import json, re

def load():
    with open("data/books.json") as f:
        return json.load(f)

def test_unique_titles():
    data = load()
    titles = [d["title"].strip().lower() for d in data]
    assert len(set(titles)) >= 15, "❌ Too many duplicate titles"

def test_price_format():
    data = load()
    assert all(re.match(r"^[£$]\d", d["price"]) for d in data), "❌ Bad price format"

def test_url_unique():
    data = load()
    urls = [d["product_url"] for d in data]
    assert len(set(urls)) == len(urls), "❌ Duplicate URLs detected"
