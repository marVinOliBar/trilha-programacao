import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("""
    UPDATE viatura
    SET quilometragem = quilometragem + ?
    WHERE situacao = 'operando'""",
    (1000,)
)

conexao.commit()
print(f"Viaturas atualizadas: {cursor.rowcount}")
conexao.close()