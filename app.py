import requests
import logging, sys
from typing import List
from pages.books_page import BooksPage

file_handler = logging.FileHandler("logs.log"); file_handler.setLevel(logging.DEBUG); file_handler.setFormatter(logging.Formatter('%(asctime)-20s  %(levelname)-6s [%(filename)s:%(lineno)d] : %(message)s'))
stream_handler = logging.StreamHandler(stream=sys.stdout); stream_handler.setLevel(logging.INFO)
logging.basicConfig(encoding='utf-8',
                    format='',
                    level=logging.DEBUG,
                    datefmt='%d-%m-%y | %H:%M:%S',
                    handlers=[file_handler, stream_handler]
                    )
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)


logger = logging.getLogger('app')

logger.info(f'Program initialisation. Loading first page')
page_content = requests.get('https://books.toscrape.com').content
page = BooksPage(page_content)  # parsed page
books: List[str] = page.books
max_page: int = page.page_count


for page_num in range(2, max_page-45):
    logger.info(f'Loading page {page_num}')
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = requests.get(url).content
    page = BooksPage(page_content)
    books.extend(page.books)
