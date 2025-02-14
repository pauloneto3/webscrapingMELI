# webscrapingMELI

## Introdução
Este código realiza a coleta e análise de produtos relacionados à busca por "Jaleco" na API do Mercado Livre. Ele coleta até 1000 produtos, extrai informações relevantes e salva os dados em um arquivo JSON e, opcionalmente, em um arquivo Excel.

---

## Requisitos
- **Python 3.x**
- Bibliotecas necessárias:
  - `requests`: Para fazer requisições HTTP à API do Mercado Livre.
  - `pandas`: Para manipulação e análise de dados.
  - `json`: Para manipulação de arquivos JSON.

Instale as bibliotecas com o seguinte comando:
```bash
pip install requests pandas
```

---

## Estrutura do Código

### 1. Importação de Bibliotecas
```python
import requests
import json
import pandas as pd
```

### 2. Definições da Busca
- A busca é realizada por meio da API do Mercado Livre, utilizando a palavra-chave "Jaleco".
- A URL base é configurada para o site do Mercado Livre Brasil (MLB).

```python
query = "Jaleco"
base_url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"
```

### 3. Coleta de Produtos
- O código faz requisições paginadas à API, coletando até 1000 produtos.
- Os produtos são armazenados em uma lista (`all_products`) e salvos em um arquivo JSON.

```python
all_products = []
offset = 0
limit = 50  # A API retorna no máximo 50 produtos por requisição
max_results = 1000  # Limite máximo de produtos que podem ser coletados

while offset < max_results:
    url = f"{base_url}&offset={offset}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    products = data.get("results", [])
    if not products:
        break
    all_products.extend(products)
    print(f"Coletados {len(all_products)} produtos...")
    offset += limit

# Salvar os produtos em um arquivo JSON
file_name = f"meli_{query}.json"
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(all_products, file, indent=4, ensure_ascii=False)

print(f"Finalizado! Total de produtos coletados: {len(all_products)}")
```

### 4. Processamento dos Dados
- Os dados coletados são carregados do arquivo JSON.
- Informações relevantes de cada produto são extraídas e armazenadas em um DataFrame.

```python
with open(file_name, "r", encoding="utf-8") as file:
    data = json.load(file)

processed_data = []

for product in data:
    row = {
        "id": product.get("id"),
        "title": product.get("title"),
        "condition": product.get("condition"),
        "listing_type_id": product.get("listing_type_id"),
        "permalink": product.get("permalink"),
        "category_id": product.get("category_id"),
        "domain_id": product.get("domain_id"),
        "thumbnail": product.get("thumbnail"),
        "order_backend": product.get("order_backend"),
        "price": product.get("price"),
        "original_price": product.get("original_price"),
        "type": product.get("sale_price", {}).get("type"),
        "available_quantity": product.get("available_quantity"),
        "free_shipping": product.get("shipping", {}).get("free_shipping"),
        "logistic_type": product.get("shipping", {}).get("logistic_type"),
        "seller_id": product.get("seller", {}).get("id"),
        "seller_nickname": product.get("seller", {}).get("nickname"),
        "state_id": product.get("address", {}).get("state_id"),
        "state_name": product.get("address", {}).get("state_name"),
        "city_name": product.get("address", {}).get("city_name")
    }
    processed_data.append(row)

df = pd.DataFrame(processed_data)
print(df.head())
```

### 5. Salvamento dos Dados (Opcional)
- O DataFrame pode ser salvo em um arquivo Excel para análise posterior.

```python
df.to_excel(f"meli_{query}.xlsx", index=False)
```

---

## Execução
1. Execute o código em um ambiente Python com as bibliotecas necessárias instaladas.
2. O código coletará os dados da API do Mercado Livre e salvará os resultados em um arquivo JSON (`meli_Jaleco.json`).
3. Os dados serão processados e exibidos em um DataFrame.
4. Opcionalmente, os dados podem ser salvos em um arquivo Excel (`meli_Jaleco.xlsx`).

---

## Exemplo de Saída
O DataFrame gerado contém as seguintes colunas:
- `id`: ID do produto.
- `title`: Título do produto.
- `condition`: Condição do produto (novo, usado, etc.).
- `price`: Preço do produto.
- `available_quantity`: Quantidade disponível.
- `free_shipping`: Indica se o frete é grátis.
- `seller_nickname`: Apelido do vendedor.
- `state_name`: Estado do vendedor.
- `city_name`: Cidade do vendedor.

---

## Contribuição
Se você encontrar problemas ou tiver sugestões de melhoria, sinta-se à vontade para contribuir.
