import os
import pandas as pd
from Dados.Extracao import get_all_categories, extract_books_from_category

# Obter o diretório atual do módulo
dir_atual = os.path.dirname(__file__)

# Definir o caminho do arquivo CSV
CSV = os.path.join(dir_atual, "base_livros.csv")


# Verifica se o CSV existe. Se não, faz Extracaoing e cria o arquivo.
def banco_dados():
    if os.path.exists(CSV):
        books = pd.read_csv(CSV)
    else:
        categorias_list = get_all_categories()
        all_books = []
        IDrecorrente = 0
        for cat in categorias_list:
            livros, IDrecorrente = extract_books_from_category(cat["name"], cat["url"], IDrecorrente)
            all_books.extend(livros)
        df = pd.DataFrame(all_books)
        df.to_csv(CSV, index=False, encoding='utf-8-sig')
        books = df
    return books
