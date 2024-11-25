# Teste Analytics - Análise de Vendas 2023

## Descrição
Este projeto consiste em uma análise completa de dados de vendas do ano de 2023, incluindo geração de dataset, limpeza de dados, análises exploratórias e consultas SQL. O projeto foi desenvolvido como parte do processo seletivo para a vaga de Estagiário de Analytics.

## Estrutura do Projeto
```
TESTE_ANALYTICS_BERNARDO_TIMM/
├── data/
│   ├── processed/
│   │   ├── data_clean.csv
│   │   ├── resultado_vendas_junho.csv
│   │   ├── resultado_vendas_total.csv
│   │   └── vendas.db
│   └── raw/
│       └── vendas_raw.csv
├── docs/
│   └── relatorio_insights.md
├── notebooks/
│   ├── limpeza_dados.ipynb
│   └── visualizacoes.ipynb
├── scripts/
│   ├── criar_banco.py
│   ├── data_set.py
│   └── sql_queries.py
├── sql/
│   └── consultas_sql.sql
├── .gitignore
├── README.md
└── requirements.txt
```

## Funcionalidades
1. **Geração de Dados** (`data_set.py`)
   - Criação de dataset sintético de vendas
   - Simulação de erros propositais para demonstrar habilidades em limpeza de dados

2. **Limpeza de Dados** (`limpeza_dados.ipynb`)
   - Tratamento de valores faltantes
   - Remoção de duplicadas
   - Correção de tipos de dados
   - Validação de categorias

3. **Análise Exploratória** (`visualizacoes.ipynb`)
   - Tendências de vendas mensais
   - Análise por produto e categoria
   - Análise de produtos que mais geraram retorno e que mais venderam quantidades por mês
   - Visualizações e insights

4. **Análises SQL** (`criar_banco.py`,`sql_queries.py`, `consultas_sql.sql`)
   - Cria um database sql com python e SQLITE3 
   - Utiliza um código python para realizar queries
   - Análise de vendas mensais
   - Produtos com menores vendas em Junho 

## Requisitos
```
pandas==2.1.3
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
jupyter==1.0.0
sqlite3
```

## Instalação e Uso

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/Teste_Analytics_Bernardo_Timm.git
cd Teste_Analytics_Bernardo_Timm
```

2. **Crie e ative um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute os scripts na seguinte ordem**
```bash
python scripts/data_set.py          # Gera o dataset inicial
python scripts/criar_banco.py       # Cria o banco SQLite
python scripts/sql_queries.py       # Executa análises SQL
```

5. **Acesse os notebooks**
   - Use Jupyter Notebook ou VS Code para abrir:
     - `notebooks/limpeza_dados.ipynb`
     - `notebooks/visualizacoes.ipynb`

## Principais Resultados
- Dataset limpo com mais de 450 registros
- Análises temporais de vendas
- Identificação de padrões e tendências
- Consultas SQL para análises específicas

## Documentação Adicional
- Relatório de insights completo em `docs/relatorio_insights.md`
- Queries SQL documentadas em `sql/consultas_sql.sql`
- Notebooks com análises detalhadas em `notebooks/`


## Observações
- Os dados gerados são sintéticos e servem apenas para demonstração
- As análises consideram o período de 01/01/2023 a 31/12/2023
- Todos os valores monetários estão em Reais (BRL)

---
