import pandas as pd
import sqlite3


# Definição de função que cria o banco de dados a partir do arquivo csv limpo
def criar_banco_dados():
    try:
        # Ler o CSV limpo
        print("Lendo arquivo CSV...")
        df = pd.read_csv('data/processed/data_clean.csv')
        
        # Criar conexão com o banco
        print("Criando banco de dados...")
        conn = sqlite3.connect('data/processed/vendas.db')
        
        # Converter data para formato SQLite
        df['Data'] = pd.to_datetime(df['Data'])
        
        # Salvar DataFrame como tabela SQL
        df.to_sql('vendas', conn, if_exists='replace', index=False)
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM vendas")
        total_registros = cursor.fetchone()[0]
        print(f"Total de registros inseridos: {total_registros}")
        
        conn.close()
        print("Banco de dados criado com sucesso!")
        
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")

if __name__ == "__main__":
    criar_banco_dados()