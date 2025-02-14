import requests
import json
import pandas as pd

# Definições da busca
query = "Jaleco"
base_url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"

# Lista para armazenar todos os produtos
all_products = []
offset = 0
limit = 50  # A API retorna no máximo 50 por vez
max_results = 1000  # Mercado Livre só permite acessar até 1000 resultados

print("Iniciando coleta de produtos...")

while offset < max_results:
    # Faz a requisição com o offset atualizado
    url = f"{base_url}&offset={offset}&limit={limit}"
    response = requests.get(url)
    data = response.json()

    # Extraindo os produtos
    products = data.get("results", [])
    if not products:
        break  # Sai do loop se não houver mais produtos

    # Adiciona todos os produtos com todos os atributos
    all_products.extend(products)

    print(f"Coletados {len(all_products)} produtos...")

    # Atualiza o offset para a próxima página
    offset += limit

# Salvando todos os produtos em um arquivo JSON
file_name_json = f"meli_{query}.json"
with open(file_name_json, "w", encoding="utf-8") as file:
    json.dump(all_products, file, indent=4, ensure_ascii=False)

print(f"Coleta finalizada! Total de produtos coletados: {len(all_products)}")
print(f"Dados salvos em: {file_name_json}")

# Processamento dos dados coletados
print("Processando os dados coletados...")

# Carregar o JSON do arquivo
with open(file_name_json, "r", encoding="utf-8") as file:
    data = json.load(file)

# Criar uma lista para armazenar os dados tratados
processed_data = []

# Percorrer os produtos e extrair informações
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

# Criar DataFrame
df = pd.DataFrame(processed_data)

# Exibir as primeiras linhas
print("\nExemplo dos dados processados:")
print(df.head())

# Salvar o DataFrame em um arquivo Excel
file_name_excel = f"meli_{query}.xlsx"
df.to_excel(file_name_excel, index=False)

print(f"Dados processados salvos em: {file_name_excel}")
print("Processamento concluído!")
