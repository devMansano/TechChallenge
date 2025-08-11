import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# Site para a extração
BASE_URL = 'http://books.toscrape.com/'

# Realiza a extração de todas as categorias 
def get_all_categories():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, 'html.parser')
    category_elements = soup.select('div.side_categories ul li ul li a')

    categories = []
    for cat in category_elements:
        name = cat.text.strip()
        rel_link = cat['href']
        full_link = urljoin(BASE_URL, rel_link)
        categories.append({"name": name, "url": full_link})
    
    return categories

# Realiza a extração dos livros a partir de cada categoria
def extract_books_from_category(category_name, category_url,IDstart=0):
    books = []
    next_page = category_url
    IDrecorrente = IDstart
    while next_page:
        res = requests.get(next_page)
        soup = BeautifulSoup(res.content, 'html.parser')
        book_elements = soup.select('article.product_pod')

        for book in book_elements:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text.strip()
            availability = book.select_one('.availability').text.strip()
            rating = book.p['class'][1]
            partial_url = book.h3.a['href']
            full_url = urljoin(next_page, partial_url)
            img_src = book.select_one('img')['src']
            img_url = urljoin(next_page, img_src)

            books.append({
                "Id": IDrecorrente,
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "url": full_url,
                "image_url": img_url,
                "category": category_name
            })
            IDrecorrente += 1
        next_btn = soup.select_one("li.next a")
        next_page = urljoin(next_page, next_btn['href']) if next_btn else None

    return books, IDrecorrente
