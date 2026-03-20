import time
from services.job_manager import JobManager
from services.crawler_service import CrawlerService
from utils.file_store import load_visited_urls

manager = JobManager()
manager.visited_set.clear()

crawler = CrawlerService(manager)

job_id = crawler.create_crawler(
    origin_url="https://example.com/",
    max_depth=0,
    hit_rate_seconds=0,
    max_urls_to_visit=1,
    queue_capacity=10
)

start_time = time.time()
while time.time() - start_time < 10:
    job = crawler.get_crawler_status(job_id)
    if job["status"] in ("completed", "failed"):
        break
    time.sleep(0.5)

assert job["status"] == "completed"
assert job["processed_count"] == 1
assert job["queued_count"] == 0
assert job["throttled"] == False

print("Phase 6 tests passed!")
