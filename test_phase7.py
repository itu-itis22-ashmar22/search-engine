import os
from services.job_manager import JobManager
from services.search_service import SearchService

manager = JobManager()
searcher = SearchService(manager)

manager.word_file_lock.acquire()
with open("storage/words/a.data", "w") as f:
    f.write("apple\thttps://site.com/a\thttps://site.com/start\t1\t5\n")
    f.write("apple\thttps://site.com/b\thttps://site.com/start\t2\t7\n")
with open("storage/words/b.data", "w") as f:
    f.write("banana\thttps://site.com/a\thttps://site.com/start\t1\t3\n")
manager.word_file_lock.release()

res = searcher.search("apple")
assert len(res) == 2
assert res[0]["relevant_url"] == "https://site.com/b"
assert res[1]["relevant_url"] == "https://site.com/a"

res2 = searcher.search("apple banana")
assert len(res2) == 2
assert res2[0]["relevant_url"] == "https://site.com/a"
assert res2[0]["total_frequency"] == 8
assert res2[1]["relevant_url"] == "https://site.com/b"
assert res2[1]["total_frequency"] == 7

print("Phase 7 tests passed!")
