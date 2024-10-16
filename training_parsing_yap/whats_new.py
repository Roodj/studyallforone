import requests_cache
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from tqdm import tqdm

URL = 'https://docs.python.org/3/whatsnew/'
url_lst = []


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(URL)
    soup = BeautifulSoup(response.text, features='lxml')

    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})

    div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})

    sections_by_python = div_with_ul.find_all('li', attrs={'class': 'toctree-l1'})

    # Печать первого найденного элемента.
    results = []
    for section in tqdm(sections_by_python):
        version_a_tag = section.find('a')

        href = version_a_tag['href']
        version_link = urljoin(URL, href)
        cute_response = session.get(version_link)
        cute_response.encoding = 'utf-8'
        cute_soup = BeautifulSoup(cute_response.text, features='lxml')
        h1 = cute_soup.find('h1').text
        dl = cute_soup.find('dl').text
        dl_text = dl.replace('\n', ' ')
        # На печать теперь выводится переменная dl_text — без пустых строчек.
        results.append((version_link, h1, dl_text))  
    for row in results:
        print(*row)
        
         