from app import books
from typing import Iterator

USER_CHOICE = '''Enter one of the following
- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit
Enter your choice: '''


def print_best_books() -> None:
    best_books = sorted(books, key=lambda x: (x.rating, x.price), reverse=True)[:5]
    print('_____Best 5 books_____')
    for book in best_books:
        print(book)
    print('_______________________________')


def print_cheapest_books() -> None:
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    print('_____Cheapest 5 books_____')
    for book in cheapest_books:
        print(book)
    print('_______________________________')


def print_next_availiable_book() -> Iterator:
    for book in books:
        yield book


next_book = print_next_availiable_book()

while (user_input := input(USER_CHOICE)) != 'q':
    if user_input == 'b':
        print_best_books()
    elif user_input == 'c':
        print_cheapest_books()
    elif user_input == 'n':
        print(next(next_book))
    else:
        print('Invalid option, try again!')
