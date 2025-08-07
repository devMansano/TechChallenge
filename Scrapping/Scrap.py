import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = 'http://books.toscrape.com/'

# Função para extrair todas as categorias de livros disponíveis no site
def get_all_categories():
    res = requests.get(BASE_URL) # Faz a requisição da página principal
    soup = BeautifulSoup(res.text, 'html.parser') # Faz o parsing do conteúdo HTML da página
    category_elements = soup.select('div.side_categories ul li ul li a') # Seleciona todos os links de categorias no menu lateral
    categories = [] # Lista onde as categorias serão armazenadas
    
    for cat in category_elements:
        
        name = cat.text.strip() # Extrai o nome da categoria (removendo espaços em branco)
        rel_link = cat['href'] # Extrai o link relativo da categoria
        full_link = urljoin(BASE_URL, rel_link) # Constrói a URL absoluta
        categories.append({"name": name, "url": full_link})  # Adiciona o dicionário com nome e URL à lista
    
    return categories # Retorna a lista de categorias

#Função para Extrair dados dos livros
def extract_books_from_category(category_name, category_url,IDstart=0):
    
    books = []  # Lista onde os dados dos livros serão armazenados
    next_page = category_url # URL da página atual, começa com a URL da categoria
    IDrecorrente = IDstart  # ID inicial para os livros, usado para identificação única
    
    while next_page: # Loop que continua enquanto houver uma próxima página na categoria
        res = requests.get(next_page)  # Faz a requisição da página atual
        soup = BeautifulSoup(res.content, 'html.parser')  # Faz o parsing do HTML da página usando BeautifulSoup
        book_elements = soup.select('article.product_pod')  # Seleciona todos os elementos de livros na página

        for book in book_elements: # Itera sobre cada livro encontrado
            
            title = book.h3.a['title']  # Extrai o título do livro
            price = book.select_one('.price_color').text.strip() # Extrai o preço
            availability = book.select_one('.availability').text.strip()  # Extrai a disponibilidade (se está em estoque)
            rating = book.p['class'][1] # Extrai a avaliação (rating) do livro, ex: "One", "Two", etc.
            partial_url = book.h3.a['href'] # Extrai a URL parcial e cria a URL completa do livro
            full_url = urljoin(next_page, partial_url)
            img_src = book.select_one('img')['src'] # Extrai o caminho da imagem e cria a URL completa da imagem
            img_url = urljoin(next_page, img_src) 

            books.append({ # Adiciona os dados extraídos do livro à lista
                "Id": IDrecorrente,
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "url": full_url,
                "image_url": img_url,
                "category": category_name
            })
            
            IDrecorrente += 1 # Incrementa o ID para o próximo livro
            
       
        next_btn = soup.select_one("li.next a") # Verifica se há botão/link para a próxima página  
        next_page = urljoin(next_page, next_btn['href']) if next_btn else None # Se houver próxima página, atualiza a URL, senão encerra o loop

    return books, IDrecorrente  # Retorna a lista de livros e o próximo ID a ser usado
