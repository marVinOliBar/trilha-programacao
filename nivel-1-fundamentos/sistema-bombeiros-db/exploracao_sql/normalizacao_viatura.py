import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = OFF")
cursor.execute("UPDATE viatura SET prefixo = TRIM(LOWER(prefixo))")
cursor.execute("UPDATE atendimento SET prefixo = TRIM(LOWER(prefixo))")
cursor.execute("PRAGMA foreign_keys = ON")
conexao.commit()
conexao.close()