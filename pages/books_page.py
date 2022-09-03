from bs4 import BeautifulSoup  # type: ignore
from typing import List
import logging

from locators.books_page_locators import BooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('app.books_page')


class BooksPage:
    def __init__(self, page: bytes) -> None:
        logger.debug('Parsing page')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self) -> List:
        logger.debug(f'Finding all books in the page with {BooksPageLocators.BOOK})')
        return [BookParser(e) for e in self.soup.select(BooksPageLocators.BOOK)]


    @property
    def page_count(self) -> int:
        logger.debug('Finding max page count')
        pager = self.soup.select_one(BooksPageLocators.PAGER).string
        max_page = int(pager.strip().split(' ')[-1])
        logger.debug(f'Number of book catalogues: {max_page}')
        return max_page
        # pattern = 'Page [0-9]+ of ([0-9]+)'
        # matcher = re.search(pattern, pager)
        # pager = int(matcher.group(1))
        # return pager
