from utils.html_fetcher import fetch_html
from utils.html_parser import extract_text_and_links

html_sample = """<html>
  <head>
    <title>Test</title>
    <style>.x{color:red}</style>
    <script>console.log("ignore me")</script>
  </head>
  <body>
    <h1>Hello Crawler</h1>
    <p>This is a parser test.</p>
    <a href="/about">About</a>
    <a href="https://example.com/contact">Contact</a>
    <a href="mailto:test@example.com">Mail</a>
  </body>
</html>"""

text, links = extract_text_and_links(html_sample, "https://example.com/start")

assert "Hello Crawler" in text
assert "This is a parser test." in text
assert "About" in text
assert "Contact" in text
assert "Mail" in text
assert ".x{color:red}" not in text
assert "console.log" not in text

assert links == ["https://example.com/about", "https://example.com/contact"]

# Test Fetcher
status, ctype, body = fetch_html("https://example.com/")
assert 200 <= status < 300
assert "text/html" in ctype
assert body

status2, ctype2, body2 = fetch_html("https://this-domain-should-not-exist.invalid/")
assert status2 == 0

print("Phase 4 tests passed!")
