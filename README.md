# webscrapingMELI


Este projeto realiza a coleta e análise de produtos relacionados a uma busca específica (por exemplo, "Jaleco") na API do Mercado Livre. Ele coleta até 1000 produtos, extrai informações relevantes e salva os dados em arquivos JSON e Excel para análise posterior.

---

## Sumário

1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Requisitos](#requisitos)
4. [Instalação](#instalação)
5. [Uso](#uso)
6. [Estrutura do Código](#estrutura-do-código)
7. [Exemplos de Saída](#exemplos-de-saída)
8. [Arquivos Gerados](#arquivos-gerados)
9. [Contribuição](#contribuição)

---

## Visão Geral

O projeto utiliza a API do Mercado Livre para coletar dados de produtos com base em uma palavra-chave de busca. Os dados coletados são processados e organizados em três DataFrames:

1. **Anúncios**: Contém informações sobre os produtos, como título, preço, condição, etc.
2. **Vendedores**: Contém informações sobre os vendedores, como ID e apelido.
3. **Categorias**: Contém informações sobre as categorias dos produtos, como nome e caminho hierárquico.

Os dados são salvos em arquivos JSON e Excel para facilitar a análise e o compartilhamento.

---

## Funcionalidades

- Coleta de até 1000 produtos da API do Mercado Livre.
- Extração de informações detalhadas sobre produtos, vendedores e categorias.
- Salvamento dos dados em arquivos JSON e Excel.
- Separação dos dados em DataFrames para facilitar a análise.

---

## Requisitos

- **Python 3.x**
- Bibliotecas necessárias:
  - `requests`: Para fazer requisições HTTP à API do Mercado Livre.
  - `pandas`: Para manipulação e análise de dados.
  - `json`: Para manipulação de arquivos JSON.

---

## Instalação

4. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-mercado-livre.git
   cd analise-mercado-livre
   ```

5. Instale as dependências:
   ```bash
   pip install requests pandas
   ```

---

## Uso

6. Execute o script Python:
   ```bash
   python analise_meli.py
   ```

7. O script coletará os dados da API do Mercado Livre e salvará os resultados em:
   - Um arquivo JSON (`meli_Jaleco.json`) com todos os produtos coletados.
   - Três arquivos Excel:
     - `meli_Jaleco_anuncios.xlsx`: Contém os anúncios.
     - `meli_Jaleco_sellers.xlsx`: Contém os vendedores.
     - `meli_Jaleco_categories.xlsx`: Contém as categorias.

8. Analise os arquivos gerados ou integre-os ao seu fluxo de trabalho.

---

## Estrutura do Código

O código está organizado nas seguintes etapas:

9. **Coleta de Dados**:
   - Faz requisições paginadas à API do Mercado Livre.
   - Coleta até 1000 produtos com base na palavra-chave fornecida.

10. **Processamento dos Dados**:
   - Extrai informações relevantes dos produtos, vendedores e categorias.
   - Remove duplicações de vendedores e categorias.

11. **Salvamento dos Dados**:
   - Salva os dados processados em arquivos JSON e Excel.

---

## Exemplos de Saída

### DataFrame de Anúncios (`df_anuncios`):
| id           | title                                      | condition | seller_id | category_id | ... |
|--------------|--------------------------------------------|-----------|-----------|-------------|-----|
| MLB2087266827| Jaleco C/ziper Feminino Colorido Acinturado| new       | 541300869 | MLB277428   | ... |

### DataFrame de Vendedores (`df_sellers`):
| seller_id | seller_nickname |
|-----------|-----------------|
| 541300869 | MUNDODOJALECO   |

### DataFrame de Categorias (`df_categories`):
| category_id | category_name       | category_path                     |
|-------------|---------------------|-----------------------------------|
| MLB277428   | Jalecos             | Moda > Roupas > Jalecos           |

---

## Arquivos Gerados

- **`meli_Jaleco.json`**: Contém todos os produtos coletados da API, com todos os atributos disponíveis.
- **`meli_Jaleco_anuncios.xlsx`**: Contém os anúncios processados.
- **`meli_Jaleco_sellers.xlsx`**: Contém os vendedores processados.
- **`meli_Jaleco_categories.xlsx`**: Contém as categorias processadas.

---

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

12. Faça um fork do projeto.
13. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
14. Commit suas mudanças (`git commit -m 'Adicionando nova feature'`).
15. Push para a branch (`git push origin feature/nova-feature`).
16. Abra um Pull Request.

---

## Contato

Se tiver dúvidas ou sugestões, entre em contato:

- **Nome**: Paulo Neto
- **Email**: pn.oliveira36@hotmail.com
- **GitHub**: https://github.com/pauloneto3
