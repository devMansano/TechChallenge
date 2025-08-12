# Exemplos de retorno para cada rota da API

---

## 1️⃣ Listar todos os livros
**Rota:** `/livros/api/v1/livros`  
**Exemplo de saída:**  
![Exemplo - Listar Livros](Exemplos/listar_livros.png)

---

## 2️⃣ Buscar livro por ID
**Rota:** `/api/v1/id/234`  
**Exemplo de saída:**  
![Exemplo - Buscar por ID](Exemplos/id.png)

---

## 3️⃣ Listar todas as categorias
**Rota:** `/api/v1/categorias/`  
**Exemplo de saída:**  
![Exemplo - Categorias](Exemplos/categorias.png)

---

## 4️⃣ Buscar livro por título e/ou categoria
**Rota:** `/api/v1/busca/?titulo=Starlark`  
**Exemplo de saída (Titulo):**  
![Exemplo - Busca com Filtros](Exemplos/busca_titulo.png)  
**Rota:** `/api/v1/busca/?categoria=Travel`  
**Exemplo de saída (Categoria):**  
![Exemplo - Busca com Filtros](Exemplos/busca_categoria.png)  
**Rota:** `/api/v1/busca/?titulo=Starlark&categoria=Crime`  
**Exemplo de saída (Titulo e/ou Categoria):**  
![Exemplo - Busca com Filtros](Exemplos/busca_titulo_categoria.png)

---

## 5️⃣ Testar conexão com a API
**Rota:** `/api/v1/conexao/`  
**Exemplo de saída:**  
![Exemplo - Conexão](Exemplos/conexao.png)
