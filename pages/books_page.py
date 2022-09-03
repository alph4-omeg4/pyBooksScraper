from bs4 import BeautifulSoup
from typing import List

from locators.books_page_locators import BooksPageLocators
from parsers.book_parser import BookParser


class BooksPage:
    def __init__(self, page: bytes) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self) -> List:
        return [BookParser(e) for e in self.soup.select(BooksPageLocators.BOOK)]


    @property
    def page_count(self) -> int:
        pager = self.soup.select_one(BooksPageLocators.PAGER).string
        return int(pager.strip().split(' ')[-1])
        # pattern = 'Page [0-9]+ of ([0-9]+)'
        # matcher = re.search(pattern, pager)
        # pager = int(matcher.group(1))
        # return pager
