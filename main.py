# ============================================================
# PROJETO: Análise de Vendas no E-commerce Brasileiro
# ETAPA: Entendimento dos Dados (CRISP-DM)
# ============================================================

# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações padrão de exibição
pd.set_option('display.max_columns', None)
sns.set(style="whitegrid")

print("Bibliotecas importadas com sucesso ✅")

# ============================================================
# LEITURA DOS DATASETS
# ============================================================

# Substitua os nomes conforme seus arquivos
orders = pd.read_csv("olist_orders_dataset.csv")
order_items = pd.read_csv("olist_order_items_dataset.csv")
products = pd.read_csv("olist_products_dataset.csv")
customers = pd.read_csv("olist_customers_dataset.csv")
payments = pd.read_csv("olist_order_payments_dataset.csv")
reviews = pd.read_csv("olist_order_reviews_dataset.csv")
sellers = pd.read_csv("olist_sellers_dataset.csv")
geolocation = pd.read_csv("olist_geolocation_dataset.csv")

print("Arquivos carregados com sucesso ✅")

# ============================================================
# EXPLORAÇÃO INICIAL DOS DADOS
# ============================================================

# Visualizando dimensões de cada base
datasets = {
    "Pedidos": orders,
    "Itens do Pedido": order_items,
    "Produtos": products,
    "Clientes": customers,
    "Pagamentos": payments,
    "Avaliações": reviews,
    "Vendedores": sellers,
    "Geolocalização": geolocation
}

print("\nDimensões de cada base:")
for name, df in datasets.items():
    print(f"{name}: {df.shape[0]} linhas e {df.shape[1]} colunas")

# Exibindo primeiras linhas de cada base
for name, df in datasets.items():
    print(f"\n===== {name} =====")
    print(df.head(3))

