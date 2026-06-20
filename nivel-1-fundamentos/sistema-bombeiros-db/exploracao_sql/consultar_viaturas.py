import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM viatura")
resultado = cursor.fetchall()
print(resultado)

conexao.close()

