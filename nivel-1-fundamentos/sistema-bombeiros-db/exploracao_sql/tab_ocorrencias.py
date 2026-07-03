import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS ocorrencia")

cursor.execute("""
    CREATE TABLE ocorrencia (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        sdo INTEGER NOT NULL,
        data TEXT NOT NULL,
        tipo TEXT NOT NULL,
        local TEXT NOT NULL,
        descricao TEXT NOT NULL,
        UNIQUE (sdo, data)
    )
""")

cursor.execute("SELECT * FROM ocorrencia")
resultado = cursor.fetchall()
print(resultado)

conexao.commit()

conexao.close()