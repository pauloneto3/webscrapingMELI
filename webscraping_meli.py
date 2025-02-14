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

# Listas para armazenar dados processados
processed_anuncios = []
processed_sellers = []
processed_categories = []

# Dicionários para evitar duplicação de sellers e categories
unique_sellers = {}
unique_categories = {}

# Percorrer os produtos e extrair informações
for product in data:
    # Informações do anúncio
    anuncio = {
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
        "seller_id": product.get("seller", {}).get("id"),  # Apenas o ID do seller
        "state_id": product.get("address", {}).get("state_id"),
        "state_name": product.get("address", {}).get("state_name"),
        "city_name": product.get("address", {}).get("city_name")
    }
    processed_anuncios.append(anuncio)

    # Informações do seller (se não foi adicionado antes)
    seller = product.get("seller", {})
    seller_id = seller.get("id")
    if seller_id and seller_id not in unique_sellers:
        unique_sellers[seller_id] = {
            "seller_id": seller_id,
            "seller_nickname": seller.get("nickname")
        }

    # Informações da categoria (se não foi adicionada antes)
    category_id = product.get("category_id")
    if category_id and category_id not in unique_categories:
        # Faz uma requisição à API para obter detalhes da categoria
        category_url = f"https://api.mercadolibre.com/categories/{category_id}"
        category_response = requests.get(category_url)
        if category_response.status_code == 200:
            category_data = category_response.json()
            unique_categories[category_id] = {
                "category_id": category_id,
                "category_name": category_data.get("name"),
                "category_path": " > ".join([x["name"] for x in category_data.get("path_from_root", [])])
            }

# Criar DataFrames
df_anuncios = pd.DataFrame(processed_anuncios)
df_sellers = pd.DataFrame(list(unique_sellers.values()))
df_categories = pd.DataFrame(list(unique_categories.values()))

# Exibir as primeiras linhas de cada DataFrame
print("\nExemplo dos dados processados:")
print("\nDataFrame de Anúncios:")
print(df_anuncios.head())

print("\nDataFrame de Vendedores:")
print(df_sellers.head())

print("\nDataFrame de Categorias:")
print(df_categories.head())

# Salvar os DataFrames em arquivos Excel
file_name_excel_anuncios = f"meli_{query}_anuncios.xlsx"
file_name_excel_sellers = f"meli_{query}_sellers.xlsx"
file_name_excel_categories = f"meli_{query}_categories.xlsx"

df_anuncios.to_excel(file_name_excel_anuncios, index=False)
df_sellers.to_excel(file_name_excel_sellers, index=False)
df_categories.to_excel(file_name_excel_categories, index=False)

print(f"\nDados processados salvos em:")
print(f"- Anúncios: {file_name_excel_anuncios}")
print(f"- Vendedores: {file_name_excel_sellers}")
print(f"- Categorias: {file_name_excel_categories}")
print("Processamento concluído!")
