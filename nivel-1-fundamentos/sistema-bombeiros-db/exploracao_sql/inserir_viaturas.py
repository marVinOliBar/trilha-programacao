import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
    ("ABT-01", 45000, "central", "operando")
)

cursor.execute(
    "INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
    ("ABT-02", 87000, "norte", "manutencao")
)

cursor.execute(
    "INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
    ("ABT-03", 12000, "sul", "operando")
)

conexao.commit()

print("3 viaturas inseridas.")
conexao.close()