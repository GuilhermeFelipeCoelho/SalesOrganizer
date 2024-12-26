import sqlite3 as db

conn = db.connect('loja.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    preco_unitario REAL NOT NULL,
    quantidade_estoque INTEGER NOT NULL,
    valor_total_estoque REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor_gasto_mes REAL NOT NULL,
    faturamento_total REAL NOT NULL,
    preco_medio REAL NOT NULL,
    lucro_total REAL NOT NULL
)
''')

conn.commit()
print("Banco de dados criado com sucesso!")
conn.close()

# index do produto | nome do produto | preço unitário do produto | quantidade do produto no estoque | valor total do produto no estoque <- DB de estoque
# valor total gasto no mês | valor do faturamento total | valor do preço médio | valor do lucro total <- DB de vendas