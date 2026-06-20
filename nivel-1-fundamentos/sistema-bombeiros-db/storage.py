import sqlite3

CAMINHO_BD = "bombeiros.db"

def registrar_viatura_storage(prefixo, quilometragem, estacao, situacao):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
                (prefixo, quilometragem, estacao, situacao)
    )
    
    valor_id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    
    return valor_id