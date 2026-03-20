import time
from app import app
from utils.file_store import *
from app import manager

manager.visited_set.clear()

client = app.test_client()

# Scenario A
res = client.get('/')
assert res.status_code in (301, 302)

res = client.get('/crawler')
assert res.status_code == 200
assert b'Local Web Crawler' in res.data

# Scenario B
post_data = {
    "origin_url": "https://example.com/",
    "max_depth": "0",
    "hit_rate_seconds": "0",
    "max_urls_to_visit": "1",
    "queue_capacity": "10"
}
res = client.post('/crawler', data=post_data)
assert res.status_code in (301, 302)
location = res.headers['Location']
crawler_id = location.split('/')[-1]

# Scenario C
time.sleep(1)
res = client.get(f'/api/crawler/{crawler_id}/status')
assert res.status_code == 200
data = res.get_json()
assert data['status'] in ('completed', 'failed', 'running')

# Scenario D
res = client.get('/search?query=example')
assert res.status_code == 200
assert b'Results' in res.data

print("E2E Tests passed!")
