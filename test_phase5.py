import os
from utils.file_store import write_json, crawler_data_path, load_visited_urls
from services.job_manager import JobManager

# Setup an interrupted job test
fake_job = {
    "crawler_id": "old_job",
    "status": "running",
    "origin_url": "https://example.com/",
    "processed_count": 2
}
write_json(crawler_data_path("old_job"), fake_job)

manager = JobManager()

# Test Interrupted Job
job = manager.get_job("old_job")
assert job["status"] == "interrupted"

# Test Mark Visited
url = "https://example.com/about"
assert manager.mark_visited(url) == True
assert manager.mark_visited(url) == False

print("Phase 5 tests passed!")
