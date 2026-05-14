import sqlite3

conexao = sqlite3.connect("bombeiros.db")
cursor = conexao.cursor()

try:
    cursor.execute("INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)", ('ABT-01', 0, 'sul', 'operando'))
    print("Teste 1: passou (não deveria!)")
except sqlite3.IntegrityError as e:
    print(f"Teste 1 bloqueado: {e}")

try:
    cursor.execute("INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)", ('ABT-05', 0, None, 'operando'))
    print("Teste 2: passou (não deveria!)")
except sqlite3.IntegrityError as e:
    print(f"Teste 2 bloqueado: {e}")

try:
    cursor.execute("INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)", ('ABT-05', 0, 'sul', 'em deslocamento'))
    print("Teste 3: passou (não deveria!)")
except sqlite3.IntegrityError as e:
    print(f"Teste 3 bloqueado: {e}")
    
try:
    cursor.execute("INSERT INTO viatura (prefixo, quilometragem, estacao, situacao) VALUES (?, ?, ?, ?)", (None, 0, 'sul', 'operando'))
    print("Teste 4: passou (não deveria!)")
except sqlite3.IntegrityError as e:
    print(f"Teste 4 bloqueado: {e}")

conexao.commit()
conexao.close()