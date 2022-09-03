from async_app import books
from typing import Iterator
import logging

logger = logging.getLogger('app.menu')

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit
Enter your choice: '''


def print_best_books() -> None:
    logger.debug('Printing best books')
    best_books = sorted(books, key=lambda x: (x.rating, x.price), reverse=True)[:5]   # type: ignore
    print('_____Best 5 books_____')
    for book in best_books:
        print(book)
    print('_______________________________')


def print_cheapest_books() -> None:
    logger.debug('Printing cheapest books')
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    print('_____Cheapest 5 books_____')
    for book in cheapest_books:
        print(book)
    print('_______________________________')


def print_next_availiable_book() -> Iterator:
    for book in books:
        logger.debug('Printing next available book')
        yield book


def start() -> None:
    while (user_input := input(USER_CHOICE)) != 'q':
        logger.debug('Got user input, processing')
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapest_books()
        elif user_input == 'n':
            print(next(print_next_availiable_book()))
        else:
            logger.debug('Incorrect menu option chosen')
            print('Invalid option, try again!')

    else:
        logger.warning('Exiting program')


if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        logger.exception("main crashed. Error: %s", e)

