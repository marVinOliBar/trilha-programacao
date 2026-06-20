import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()
cursor.execute("SELECT prefixo FROM viatura WHERE situacao = 'operando'")
resultado = cursor.fetchall()

for linha in resultado:
    print(linha[0])
    
conexao.close()