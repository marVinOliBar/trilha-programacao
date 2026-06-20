import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

#cursor.execute("SELECT * FROM atendimento")

cursor.execute("""SELECT viatura.prefixo, ocorrencia.tipo,
            ocorrencia.local
            FROM atendimento 
            JOIN viatura ON atendimento.prefixo = viatura.prefixo
            JOIN ocorrencia ON atendimento.id = ocorrencia.id
""")
resultado = cursor.fetchall()



print(resultado)
conexao.commit()
conexao.close()