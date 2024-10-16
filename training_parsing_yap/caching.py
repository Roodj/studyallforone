import requests_cache
import os
from dotenv import load_dotenv

# Сохранение адреса веб-страницы в константу. Это удобно, потому 
# что при написании парсера, к адресу нужно постоянно обращаться. 
load_dotenv()
doc_url = os.getenv('MAIN_DOC_URL')

if __name__ == '__main__':
    # Сессия, кеширующая результаты загрузки страниц.
    session = requests_cache.CachedSession()
      # Очистка кеша.
    session.cache.clear()
    # Загрузка веб-страницы при помощи HTTP-метода get(). 
    response = session.get(doc_url)
    print(session.cache.urls()) 