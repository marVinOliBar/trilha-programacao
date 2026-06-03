import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("SELECT sql FROM sqlite_master WHERE name='atendimento'")
print(cursor.fetchone())

conexao.commit()
conexao.close()