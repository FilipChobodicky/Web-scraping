import requests
from bs4 import BeautifulSoup

book_list = []

for x in range(1, 51):
    # print(x)
    url = f'http://books.toscrape.com/catalogue/page-{x}.html'

    r = requests.get(url)

    # print(r.status_code)
    # print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    # print(soup)

    article = soup.find_all('article', class_ = 'product_pod')

    # print(article)



    for book in article:
        title = book.find_all('a')[1]['title']
        price = book.find('p', class_ = 'price_color').text[2:]
        instock = book.find('p', class_ = 'instock availability').text.strip()
        books = {
            'title': title,
            'price': price,
            'instock': instock
        }
        book_list.append(books)


        # print(title)
        # print(price)
        # print(instock)

# print(book_list[1])
print(len(book_list))


