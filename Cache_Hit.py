import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.fetch import fetch
import os
import time


def did_fetch(user, url):
    os.environ['USER'] = user
    t1 = time.time()
    fetch(url)
    t2 = time.time()
    if t2-t1 >= 0.1:
        return False
    return True
"""
#fetch()
_cache = {}
def fetch(url):
    user = os.environ['USER']
    if user not in _cache:
        _cache[user] = {}
    if url not in _cache[user]:
        _cache[user][url] = requests.get(url).content
    return _cache[user][url]
"""
