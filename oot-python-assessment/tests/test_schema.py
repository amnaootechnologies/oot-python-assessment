import json, os
from jsonschema import validate

def test_output_exists():
    assert os.path.exists("data/books.json"), "❌ data/books.json is missing"

def test_schema_valid():
    with open("tests/schema.json") as f:
        schema = json.load(f)
    with open("data/books.json") as f:
        data = json.load(f)
    validate(instance=data, schema=schema)
