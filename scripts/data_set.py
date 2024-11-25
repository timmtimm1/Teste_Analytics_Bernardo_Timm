import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Produtos e suas categorias
produtos = {
    'Notebook Dell': {'categoria': 'Informática', 'preco_base': 4500},
    'Notebook HP': {'categoria': 'Informática', 'preco_base': 3800},
    'Mouse Gamer': {'categoria': 'Acessórios', 'preco_base': 150},
    'Teclado Wireless': {'categoria': 'Acessórios', 'preco_base': 200},
    'Monitor 24"': {'categoria': 'Informática', 'preco_base': 1200},
    'Smartphone Samsung': {'categoria': 'Telefonia', 'preco_base': 2500},
    'iPhone': {'categoria': 'Telefonia', 'preco_base': 5000},
    'Carregador USB': {'categoria': 'Acessórios', 'preco_base': 50},
    'Webcam HD': {'categoria': 'Acessórios', 'preco_base': 180},
    'Fone Bluetooth': {'categoria': 'Acessórios', 'preco_base': 150}
}

# Gerando os dados
registros = []
data_inicial = datetime(2023, 1, 1)

# Gerando 500 registros, número um pouco mais alto para ter uma análise mais ampla 
for id in range(1, 501):
    # Escolhendo um produto aleatório
    produto = random.choice(list(produtos.keys()))
    info_produto = produtos[produto]
    # Gerando uma data aleatória em 2023
    dias_aleatorios = random.randint(0, 364)
    data = data_inicial + timedelta(days=dias_aleatorios)
    # Gerando quantidade e preço com algumas variações
    quantidade = random.randint(1, 15)
    preco = info_produto['preco_base'] * random.uniform(0.85, 1.15)  # Variação de 15% no preço
    
    registro = {
        'ID': id,
        'Data': data,
        'Produto': produto,
        'Categoria': info_produto['categoria'],
        'Quantidade': quantidade,
        'Preco': round(preco, 2)
    }
    registros.append(registro)

# Criando o DataFrame
df = pd.DataFrame(registros)

# Adicionando erros propositais para o processo de limpeza
# 1. Alguns valores nulos na quantidade
df.loc[random.sample(range(500), 13), 'Quantidade'] = np.nan

# 2. Alguns preços zerados
df.loc[random.sample(range(500), 9), 'Preco'] = 0

# 3. Algumas datas inválidas (fora de 2023)
indices_data_errada = random.sample(range(500), 17)
for idx in indices_data_errada:
    if random.random() > 0.5:
        df.loc[idx, 'Data'] = datetime(2024, 1, 1)  # Data futura
    else:
        df.loc[idx, 'Data'] = datetime(2022, 12, 31)  # Data passada

# 4. Duplicando alguns registros
registros_duplicados = df.sample(n=14)
df = pd.concat([df, registros_duplicados])

# 5. Alguns produtos com categoria errada
indices_categoria_errada = random.sample(range(500), 22)
categorias = ['Informática', 'Acessórios', 'Telefonia']
for idx in indices_categoria_errada:
    df.loc[idx, 'Categoria'] = random.choice(categorias)

# Salvando o arquivo
df.to_csv('vendas_raw.csv', index=False)

print("Total de registros no arquivo:", len(df))