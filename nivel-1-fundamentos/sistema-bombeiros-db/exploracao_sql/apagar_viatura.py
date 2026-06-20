import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("""
    DELETE FROM viatura
    WHERE prefixo = ?""",
    ("ABT-02",)
)

conexao.commit()
print(f"Linhas apagadas: {cursor.rowcount}")
conexao.close()