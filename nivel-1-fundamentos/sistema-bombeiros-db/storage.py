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

def buscar_viatura_storage(termo):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    
    cursor.execute("SELECT prefixo, quilometragem, estacao, situacao FROM viatura WHERE prefixo LIKE ?",
                   (f"%{termo}%",)
    )
    
    resultado = cursor.fetchall()
    conexao.close()
    
    return resultado

def remover_viatura_storage(prefixo):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("DELETE FROM viatura WHERE prefixo = ?",
                   (prefixo,))
    resultado = cursor.rowcount
    conexao.commit()
    conexao.close()
    return resultado

def editar_viatura_storage(prefixo, quilometragem, estacao, situacao):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("UPDATE viatura SET quilometragem = ?, estacao = ?, situacao = ? WHERE prefixo = ?",
                   (quilometragem, estacao, situacao, prefixo))
    resultado = cursor.rowcount
    conexao.commit()
    conexao.close()
    return resultado

def listar_viatura_storage():
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("SELECT prefixo, quilometragem, estacao, situacao FROM viatura")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def registrar_ocorrencia_storage(sdo, data, tipo, local, descricao):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute("INSERT INTO ocorrencia (sdo, data, tipo, local, descricao) VALUES (?, ?, ?, ?, ?)",
                   (sdo, data, tipo, local, descricao)
                   
    )
    resultado = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return resultado

registrar_ocorrencia_storage(2, "2026-06-29", "incêndio", "rua x", "teste")