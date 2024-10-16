import requests_cache 
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm


MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == "__main__":

    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    
    sidebar = soup.find('div', attrs={'class':'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')

    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
        else:
            raise Exception('Ничего не нашлось')
        
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    results = []
    for a_tag in a_tags:
                link = a_tag['href']
                if re.search(pattern,  a_tag.text):
                    version = re.search(pattern, a_tag.text).group('version')
                    status = re.search(pattern, a_tag.text).group('status')
                    results.append((link, version, status))
                else:
                    results.append((link, version))
    for row in results:
        print(*row) 
    