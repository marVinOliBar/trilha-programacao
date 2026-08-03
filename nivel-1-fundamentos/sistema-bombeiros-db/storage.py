import sqlite3

CAMINHO_BD = "bombeiros.db"

def registrar_viatura_storage(prefixo, quilometragem, estacao, situacao):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)",
                    (prefixo, quilometragem, estacao, situacao)
        )
        valor_id = cursor.lastrowid
        conexao.commit()
    finally:
        conexao.close()
    return valor_id

def buscar_viatura_storage(termo):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("SELECT prefixo, quilometragem, estacao, situacao FROM viatura WHERE prefixo LIKE ?",
                    (f"%{termo}%",)
        )
        resultado = cursor.fetchall()
    finally:
        conexao.close()
    
    return resultado

def remover_viatura_storage(prefixo):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("DELETE FROM viatura WHERE prefixo = ?",
                   (prefixo,))
        resultado = cursor.rowcount
        conexao.commit()
    finally:
        conexao.close()
    return resultado

def editar_viatura_storage(prefixo, quilometragem, estacao, situacao):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("UPDATE viatura SET quilometragem = ?, estacao = ?, situacao = ? WHERE prefixo = ?",
                   (quilometragem, estacao, situacao, prefixo))
        resultado = cursor.rowcount
        conexao.commit()
    finally:
        conexao.close()
    return resultado

def listar_viatura_storage():
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("SELECT prefixo, quilometragem, estacao, situacao FROM viatura")
        resultado = cursor.fetchall()
    finally:
        conexao.close()
    return resultado

def registrar_ocorrencia_storage(sdo, data, tipo, local, descricao):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("INSERT INTO ocorrencia (sdo, data, tipo, local, descricao) VALUES (?, ?, ?, ?, ?)",
                    (sdo, data, tipo, local, descricao)
                    
        )
        resultado = cursor.lastrowid
        conexao.commit()
    finally:
        conexao.close()
    return resultado

def listar_ocorrencia_storage():
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("SELECT sdo, data, tipo, local, descricao FROM ocorrencia")
        resultado = cursor.fetchall()
    finally:
        conexao.close()
    return resultado

def remover_ocorrencia_storage(sdo, data):
    conexao = sqlite3.connect(CAMINHO_BD)
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        cursor.execute("DELETE FROM ocorrencia WHERE sdo = ? AND data = ?",
                    (sdo, data))
        resultado = cursor.rowcount
        conexao.commit()
    finally:
        conexao.close()
    return resultado