import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

BASE_URL = 'http://books.toscrape.com/'

def get_all_categories():
    res = requests.get(BASE_URL)
    soup = BeautifulSoup(res.text, 'html.parser')

    category_elements = soup.select('div.side_categories ul li ul li a')
    categories = []
    for cat in category_elements:
        name = cat.text.strip()
        rel_link = cat['href']
        full_link = urljoin(BASE_URL, rel_link)
        categories.append((name, full_link))

    return categories

def extract_books_from_category(category_name, category_url):
    books = []
    next_page = category_url

    while next_page:
        res = requests.get(next_page)
        soup = BeautifulSoup(res.content, 'html.parser', from_encoding='utf-8')

        book_elements = soup.select('article.product_pod')
        print(f"{category_name} - {len(book_elements)} livros em: {next_page}")

        for book in book_elements:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text.strip()
            availability = book.select_one('.availability').text.strip()
            rating = book.p['class'][1]
            partial_url = book.h3.a['href']
            full_url = urljoin(next_page, partial_url)
            img_src = book.select_one('img')['src'] 
            img_url = urljoin(next_page, img_src)

            #Grava as informações dentro de cada coluna
            books.append({
                "title": title,
                "price": price, 
                "availability": availability,
                "rating": rating,
                "url": full_url,
                "image_url": img_url, 
                "category": category_name
            })

        next_btn = soup.select_one("li.next a")
        if next_btn:
            next_href = next_btn['href']
            next_page = urljoin(next_page, next_href)
        else:
            next_page = None

    return books

# Roda o scraping para todas as categorias
all_books = []
categories = get_all_categories()

for name, link in categories:
    books = extract_books_from_category(name, link)
    all_books.extend(books)

# Salva em CSV
df = pd.DataFrame(all_books)
df.to_csv("books_complete.csv", index=False, encoding='utf-8-sig')
print(f"\nTotal de livros coletados: {len(df)}")