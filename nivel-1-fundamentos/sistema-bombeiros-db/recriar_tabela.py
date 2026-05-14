import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("""
    DROP TABLE
    IF EXISTS viatura"""
)

print("Tabela antiga removida.")

cursor.execute("""
    CREATE TABLE viatura (
        prefixo TEXT PRIMARY KEY NOT NULL,
        quilometragem INTEGER NOT NULL,
        estacao TEXT NOT NULL,
        situacao TEXT NOT NULL CHECK (situacao IN ('operando', 'manutencao', 'baixada'))
    )
""")

print("Tabela viatura recriada com constraints.")

cursor.execute(
    "INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
    ("ABT-01", 45000, "central", "manutencao")
)

cursor.execute(
    "INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
    ("ABT-03", 1300, "sul", "operando")
)

print("2 viatura reinseridas.")

conexao.commit()
conexao.close()