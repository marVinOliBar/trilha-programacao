import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("DROP TABLE IF EXISTS atendimento")

cursor.execute("""
    CREATE TABLE atendimento (
        prefixo TEXT NOT NULL,
        id INTEGER NOT NULL,
        PRIMARY KEY (prefixo, id),
        FOREIGN KEY (prefixo) REFERENCES viatura(prefixo),
        FOREIGN KEY (id) REFERENCES ocorrencia(id)        
    )
""")

cursor.execute("INSERT INTO atendimento (prefixo, id) VALUES (?,?)",
               ("ABT-01", 1)
)

cursor.execute("SELECT * FROM atendimento")
resultado = cursor.fetchall()
print(resultado)

conexao.commit()
conexao.close()
