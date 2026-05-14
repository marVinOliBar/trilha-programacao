import sqlite3

conexao = sqlite3.connect("bombeiros.db")
print("Conexão aberta.")

cursor = conexao.cursor()
print("Cursor criado.")

cursor.execute("""
               CREATE TABLE viatura(
                   prefixo TEXT,
                   quilometragem INTEGER,
                   estacao TEXT,
                   situacao TEXT
               )
""")
print("Tabela viatura criada.")

conexao.commit()
print("Mudanças salvas.")

conexao.close()
print("Conexão fechada.")