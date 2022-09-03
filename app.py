import requests

from pages.books_page import BooksPage


page_content = requests.get('https://books.toscrape.com').content
page = BooksPage(page_content)  # parsed page
books = page.books
max_page = page.page_count

for page_num in range(2, max_page):
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    page_content = requests.get(url).content
    page = BooksPage(page_content)
    books.extend(page.books)
