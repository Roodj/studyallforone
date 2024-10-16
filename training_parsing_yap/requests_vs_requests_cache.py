from time import sleep
from tqdm import tqdm
import requests_cache
import requests

URL = "http://httpbin.org/delay/3"

if __name__ == '__main__':
    for i in tqdm(range(3), desc='без кеша'):
        requests.get(URL)
    for i in tqdm(range(3), desc='кеша'):
            cached_session = requests_cache.CachedSession()
            cached_session.get(URL)
    cached_session.cache.clear()