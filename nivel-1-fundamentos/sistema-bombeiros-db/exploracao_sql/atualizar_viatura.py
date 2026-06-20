import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("""
    UPDATE viatura
    SET situacao = ?
    WHERE prefixo = ?""",
    ("manutencao", "ABT-01")    
)

conexao.commit()
print(f"Linhas atualizadas: {cursor.rowcount}")
conexao.close()