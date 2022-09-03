import requests
import logging, sys
from typing import List
import aiohttp
import asyncio
import async_timeout
import time

from pages.books_page import BooksPage


fh = logging.FileHandler("logs.log");  fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler(stream=sys.stdout); sh.setFormatter(logging.Formatter(''))
logging.basicConfig(encoding='utf-8',
                    format='%(asctime)-20s %(levelname)-6s [%(filename)s:%(lineno)d] : %(message)s',
                    level=logging.INFO,
                    datefmt='%d-%m-%y | %H:%M:%S',
                    handlers=[fh, sh]
                    )
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('charset_normalizer').setLevel(logging.WARNING)

logger = logging.getLogger('app')

#######################################################################################################################

logger.info(f'Program initialisation')
page_content = requests.get('https://books.toscrape.com').content
page = BooksPage(page_content)  # parsed page
books: List[str] = page.books
max_page: int = page.page_count


async def fetch_page(url: str):
    page_start_time = time.time()
    async with async_timeout.timeout(10):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                logger.debug(f'Loading page took {time.time() - page_start_time}')
                return await response.text()


async def main():
    tasks = [fetch_page(url) for url in urls]
    return await asyncio.gather(*tasks)


urls = [f'https://books.toscrape.com/catalogue/page-{page_num + 1}.html' for page_num in range(1, max_page)]

start_time = time.time()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
pages = asyncio.run(main())

end_time = time.time()

for page_content in pages:
    logger.debug(f'Making BooksPage')
    page = BooksPage(page_content)
    books.extend(page.books)

logger.info(f'Total load time is {end_time- start_time} for {max_page} pages and {len(books)} books')
