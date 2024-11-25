import sqlite3
import pandas as pd

# Definir função para conectar com o banco de dados 
def conectar_banco():
    try:
        conn = sqlite3.connect(r'C:\Users\berna\Teste_Analytics_Bernardo_Timm\data\processed\vendas.db')
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para executar Queries e retornar os resultados

def executar_query(conn, query, descricao=""):
    try:
        print(f"{descricao}")
        resultado = pd.read_sql_query(query, conn)
        print(resultado.to_string())
        return resultado
    except sqlite3.Error as e:
        print(f"Erro ao executar query: {e}")
        return None
    
# Função principal que define as queries solicitadas

def main():
    # Estabelecer conexão
    conn = conectar_banco()
    if not conn:
        return
    
    # Query 1: Total de vendas por produto
    query1 = """
    SELECT 
        Produto,
        Categoria,
        ROUND(SUM(Quantidade * Preco), 2) as Total_Vendas
    FROM vendas
    GROUP BY Produto, Categoria
    ORDER BY Total_Vendas DESC;
    """
    
    # Query 2: Produtos com menores vendas em junho
    query2 = """
    SELECT 
        Produto,
        ROUND(SUM(Quantidade * Preco), 2) as Total_Vendas
    FROM vendas
    WHERE strftime('%m', Data) = '06'
    GROUP BY Produto
    ORDER BY Total_Vendas ASC;
    """
    
    # Executando e salvando resultados
    print("RESULTADOS DAS QUERIES SQL")
    
    resultado1 = executar_query(conn, query1, "1. Total de vendas por produto (ordenado por valor total):")
    
    resultado2 = executar_query(conn, query2, "2. Produtos com menores vendas em junho:")
    
    # Salvando resultados em arquivos CSV 
    if resultado1 is not None:
        resultado1.to_csv('data/processed/resultado_vendas_total.csv', index=False)
        
    if resultado2 is not None:
        resultado2.to_csv('data/processed/resultado_vendas_junho.csv', index=False)
    
    # Fechando conexão
    conn.close()
    
    print("- data/processed/resultado_vendas_total.csv")
    print("- data/processed/resultado_vendas_junho.csv")

if __name__ == "__main__":
    main()