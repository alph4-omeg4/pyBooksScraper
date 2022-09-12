# pyBooksScraper
Async web scraper 

asyncio, aiohttp
beatifulsoup4
logging

example on books.toscrape.com:

1. Scraping first page and parsing it to determine number of pages in catalogue
2. Scraping remaining pages
3. Parse all pages for required info : name, link, price, rating
4. Output trunk of desired selection, such as: best rated books, cheapest books or just 1 available book by order
