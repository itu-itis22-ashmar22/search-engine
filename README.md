# Web Crawler Demo

## Overview
This project is a local prototype web crawler and live search engine built for the assignment. It starts from an origin URL, crawls to depth k, prevents duplicate crawling, indexes words to filesystem buckets, and supports searching while crawlers are active.

## Features
- background crawler jobs
- visited URL deduplication
- configurable crawl depth
- configurable hit rate
- queue-capacity-based back pressure
- live crawler status page
- filesystem-backed word index
- live search over indexed content
- local execution on localhost

## Architecture

### Crawler Service
Handles crawl creation and page indexing.

### Search Service
Handles query execution against word index files.

### Storage Layer
Handles metadata, queue, logs, visited URLs, and word buckets.

### Web UI
Handles crawl creation, status viewing, and search.

## Storage Layout
storage/
├── crawlers/
├── logs/
├── queues/
├── words/
└── visited_urls.data

- The visited file prevents duplicate crawling.
- Crawler data file stores job metadata and counters.
- Queue file supports visibility and partial recovery.
- Log file supports observability.
- Word files support search by alphabetical partitioning.

## How to Run

```bash
python -m venv .venv
# activate venv
# On Windows: .venv\Scripts\activate
# On Unix: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open your browser at the local address printed by Flask, usually http://127.0.0.1:5000.

## How to Use

**Start a crawler**
open /crawler, fill in origin URL, depth, hit rate, max URLs, queue capacity, and submit form.

**Monitor a crawler**
open crawler status page and watch logs, queue preview, counts, and throttled state update live.

**Search**
open /search, enter a query, review results as (relevant_url, origin_url, depth). Partial results may appear while crawlers are running.

## Search Semantics
Search is exact keyword match over indexed tokens. Each matching record links the query word to the relevant URL, origin URL, depth, and frequency. Results are aggregated and sorted by total frequency descending, depth ascending.

## Back Pressure
Each crawler supports a hit rate delay between requests. Each crawler also has queue capacity. Once capacity is reached, additional discovered links are not enqueued, and the crawler state exposes whether it is currently throttled.

## Example Workflow
Start a crawl from https://example.com/ with depth 1 and max 10 URLs.
Open the status page and observe processed pages and queue growth.
Open /search and query a known indexed word.
Repeat the query while the crawler is still running to observe new results.

## Limitations
- filesystem storage instead of database
- no intra-crawler parallel page processing
- exact-match search only
- no robots.txt enforcement
- no JavaScript rendering
- no advanced ranking

## Future Improvements
- move index/storage to DB or key-value store
- better indexing structure
- stronger crawl politeness and retry logic
- advanced search ranking
- better resume/recovery semantics
