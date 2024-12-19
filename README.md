# Sistema de Controle de Estoque de Consoles

Este projeto é uma API RESTful desenvolvida em Python com FastAPI que permite gerenciar um estoque de consoles de videogame, incluindo operações para listar, adicionar, atualizar e remover consoles. A API armazena os dados em memória utilizando listas e é ideal para fins educacionais ou prototipagem.

---

## **Funcionalidades**

- **GET /videogames**: Lista todos os consoles no estoque.
- **GET /videogames/{id}**: Retorna os detalhes de um console pelo ID.
- **POST /videogames**: Adiciona um novo console ao estoque.
- **PUT /videogames/{id}**: Atualiza as informações de um console existente pelo ID.
- **DELETE /videogames/{id}**: Remove um console do estoque pelo ID.

---

## **Entidades**

A entidade principal é o **Console**, que possui os seguintes atributos:

- `id` (int): Identificador único do console.
- `nome` (string): Nome do console.
- `quantidade` (int): Quantidade disponível no estoque.
- `preco` (float): Preço unitário do console.

Exemplo de JSON:
```json
{
  "id": 1,
  "nome": "PlayStation 5",
  "quantidade": 10,
  "preco": 4999.99
}
```

---

## **Como Executar o Projeto**

### Pré-requisitos

- Python 3.9 ou superior.
- Gerenciador de pacotes `pip`.

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/sistema-estoque-consoles.git
   cd sistema-estoque-consoles
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor:
   ```bash
   uvicorn controle_estoque:app --reload
   ```

4. Acesse a documentação interativa em:
   - [Swagger UI](http://127.0.0.1:8000/docs)
   - [Redoc](http://127.0.0.1:8000/redoc)

---

## **Como Usar a API**

### Exemplos de Requisições

#### **1. Listar todos os consoles**
- **Método:** `GET`
- **Endpoint:** `/videogames`
- **Resposta:**
  ```json
  [
    {
      "id": 1,
      "nome": "PlayStation 5",
      "quantidade": 10,
      "preco": 4999.99
    }
  ]
  ```

#### **2. Adicionar um novo console**
- **Método:** `POST`
- **Endpoint:** `/videogames`
- **Body:**
  ```json
  {
    "id": 2,
    "nome": "Xbox Series X",
    "quantidade": 5,
    "preco": 4599.99
  }
  ```

- **Resposta:**
  ```json
  {
    "id": 2,
    "nome": "Xbox Series X",
    "quantidade": 5,
    "preco": 4599.99
  }
  ```

#### **3. Atualizar um console existente**
- **Método:** `PUT`
- **Endpoint:** `/videogames/2`
- **Body:**
  ```json
  {
    "nome": "Xbox Series X",
    "quantidade": 8,
    "preco": 4499.99
  }
  ```

- **Resposta:**
  ```json
  {
    "id": 2,
    "nome": "Xbox Series X",
    "quantidade": 8,
    "preco": 4499.99
  }
  ```

#### **4. Remover um console**
- **Método:** `DELETE`
- **Endpoint:** `/videogames/2`
- **Resposta:**
  ```json
  {"mensagem": "Console removido com sucesso."}
  ```

---

## **Documentação no Postman**

1. Importe as rotas da API no Postman usando a URL base: `http://127.0.0.1:8000`.
2. Documente as requisições e salve exemplos de requisições e respostas.

---

## **Publicação no GitHub**

Suba o projeto no GitHub e inclua este arquivo `README.md` explicando:
- O problema que a API resolve.
- Como executar o projeto localmente.
- Exemplos de uso das rotas.

---

### **Contato**
Em caso de dúvidas, entre em contato pelo e-mail (rodrigs.lima17@gmail.com).

