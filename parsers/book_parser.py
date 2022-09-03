import re
import bs4  # type: ignore
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('app.book_parser')


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }


    def __init__(self, parent: bs4.element.Tag) -> None:
        logger.debug(f'New book parser created')
        self.parent = parent

    def __repr__(self) -> str:
        logger.debug('Parsing and printing out book entry')
        stars = f'stars' if self.rating > 1 else f'star'
        return f'<Book {self.title}, for {self.price} pounds, with {self.rating} {stars}>'

    @property
    def title(self) -> str:
        logger.debug('Finding book name')
        locator = BookLocators.TITLE_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug('Found book name')
        return item_name

    @property
    def link(self) -> str:
        logger.debug('Finding book link')
        locator = BookLocators.TITLE_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug('Found book link')
        return item_link

    @property
    def price(self) -> float:
        logger.debug('Finding book price')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        r_pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(r_pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug('Found book price')
        return float_price

    @property
    def rating(self) -> int:
        logger.debug('Finding book rating')
        locator = BookLocators.RATING_LOCATOR
        rating_tag = self.parent.select_one(locator)
        classes = rating_tag.attrs['class']
        rating_class = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_class[0], 0)
        logger.debug('Found book rating')
        return rating_number
