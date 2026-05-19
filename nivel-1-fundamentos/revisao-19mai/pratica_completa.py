import sqlite3

conexao = sqlite3.connect("revisao.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS produto")

# --- DDL: criar tabela do zero ---
cursor.execute("""
    CREATE TABLE produto (
        codigo TEXT PRIMARY KEY NOT NULL,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        categoria TEXT NOT NULL CHECK (categoria IN ('eletronico', 'alimento', 'roupa'))
    )               
""")

print ("Tabela produto criada.")

# --- DML: inserir três produtos ---

cursor.execute(
    "INSERT INTO produto (codigo, nome, preco, categoria) VALUES (?, ?, ?, ?)",
    ("P001", "Notebook", 3500.00, "eletronico")
)

cursor.execute(
    "INSERT INTO produto (codigo, nome, preco, categoria) VALUES (?, ?, ?, ?)",
    ("P002", "Camiseta", 49.90, "roupa")
)

cursor.execute(
    "INSERT INTO produto (codigo, nome, preco, categoria) VALUES (?, ?, ?, ?)",
    ("P003", "Arroz 5kg", 28.50, "alimento")
)

print(f"Produtos inseridos: 3")

# --- SELECT: consulta com filtro ---
cursor.execute("SELECT codigo, nome FROM produto WHERE categoria = ?", ("eletronico",))
resultado = cursor.fetchall()

print("\nProdutos eletrônicos: ")
for linha in resultado:
        print(f"    {linha[0]} - {linha[1]}")

# --- UPDATE: aumentar preço de uma categoria ---
cursor.execute(
    "UPDATE produto SET preco = preco * 1.10 WHERE categoria = ?",
    ("alimento",)
)
print(f"Produtos com preço aumentado: {cursor.rowcount}")

# --- DELETE: remover por código ---
cursor.execute("DELETE FROM produto WHERE codigo = ?", ("P002",))
print(f"Produtos apagados: {cursor.rowcount}")

# --- SELECT: final para ver o estado ---
cursor.execute("SELECT * FROM produto")
todos = cursor.fetchall()

print("\nEstado final da tabela: ")
for linha in todos:
    print(f"    {linha}")

# --- Confirma e fecha ---
conexao.commit()
conexao.close()
print("\nFim.")