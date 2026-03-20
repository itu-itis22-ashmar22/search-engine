import os
import sys
from utils.file_store import *
from utils.tokenizer import *
from utils.url_utils import *

ensure_storage_layout()
load_visited_urls()

# Storage basic check
write_json("storage/test.json", {"a": 1})
assert read_json("storage/test.json") == {"a": 1}

# Tests exact to chunk 7
assert normalize_word("Hello") == "hello"
assert normalize_word("  WORLD  ") == "world"
assert normalize_word("") == ""
assert normalize_word("AI") == "ai"

assert tokenize_text("Hello, world! Hello crawler. AI is fun in 2026.") == ["hello", "world", "hello", "crawler", "ai", "is", "fun", "in", "2026"]
assert count_words("article article test crawler crawler crawler") == {"article": 2, "test": 1, "crawler": 3}

assert normalize_url("HTTPS://Example.COM/About#team") == "https://example.com/About"
assert normalize_url("https://example.com/about/") == "https://example.com/about"
assert normalize_url("https://example.com") == "https://example.com/"
assert normalize_url("   https://example.com/docs?page=2#section") == "https://example.com/docs?page=2"

assert should_skip_url("mailto:test@example.com") == True
assert should_skip_url("javascript:void(0)") == True
assert should_skip_url("tel:+905555555555") == True
assert should_skip_url("https://example.com/file.pdf") == True
assert should_skip_url("https://example.com/image.jpg") == True
assert should_skip_url("https://example.com/page") == False
assert should_skip_url("http://example.com/page") == False

assert resolve_url("https://example.com/docs/start", "../about") == "https://example.com/about"
assert resolve_url("https://example.com/docs/start", "/team") == "https://example.com/team"
assert resolve_url("https://example.com/docs/start", "https://other.com/x") == "https://other.com/x"

print("All Phase 2 & 3 tests passed!")
