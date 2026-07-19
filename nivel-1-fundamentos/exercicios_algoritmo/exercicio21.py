"""
Problema — pedidos por cliente com nome
Duas listas: clientes (id + nome) e pedidos (client_id + valor). 
Devolve lista de dicts com nome do cliente e total gasto, ordenada do que mais gastou pro que menos gastou.
"""
clientes = [
    {"id": 1, "nome": "ana"},
    {"id": 2, "nome": "bruno"},
    {"id": 3, "nome": "carla"},
    {"id": 4, "nome": "diego"},
]

pedidos = [
    {"client_id": 1, "valor": 150.00},
    {"client_id": 2, "valor": 80.00},
    {"client_id": 1, "valor": 200.00},
    {"client_id": 3, "valor": 45.00},
    {"client_id": 2, "valor": 120.00},
    {"client_id": 1, "valor": 90.00},
    {"client_id": 3, "valor": 300.00},
]

"""
FAZ: a função recebe duas listas, clientes e pedidos, contendo dicionários, faz a junção as tabelas por meio do número
de id, comum as duas listas, depois agrupa os dados somando os valores gastos de cada cliente.
ENTRADA: lista clientes com dicionários de chaves 'id' (int) e 'nome' (str); lista pedidos com dicionarios de chaves
'client_id' (int) e 'valor' (float).
SAÍDA: lista de dicionarios de chaves 'nome' (str) e 'total' (float).
REGRA:
BLOCO 1 -
    fazer dict comprehension para cada cliente em clientes fazer um dicionario com a chave
de valor 'id' de clientes e valor a variável cliente e atribuir cada novo dicionario a variavel clientes_por_id
    
BLOCO 2 - GROUP BY sum?
    declarar variavel total_por_id e atribuir a ela um dicionario vazio
para cada pedido percorrer a lista pedidos
    declarar variavel chave e atribuir a ela o valor de 'client_id' de cada pedido
    verificar se chave não está dentro de total_por_id
        se sim, atribuir 0 ao valor da chave 'chave' dentro de total_por_id
    adicionar o 'valor' de cada pedido ao valor de chave dentro de total_por_id

BLOCO 3 - MAP de dict para list
    fazer list comprehension para cada id_cliente e valor percorrer total_por_id.items() e fazer um novo dicionário de chaves 'nome'
(com o valor da chave 'nome' de cada dicionário de clientes_por_id) e 
'total' (com o valor da variavel total dentro do dicionario de total_por_id)
e atribuir a variavel lista_nova

BLOCO 4 - SORT
    ordenar a lista_nova pelo valor da chave 'total' de maior para menor e atribuir a lista_ordenada
    
    retornar a lista_ordenada
"""

def pedidos_por_cliente(clientes, pedidos):
    clientes_por_id = {cliente['id']:cliente['nome'] for cliente in clientes}
    
    total_por_id = {}
    for pedido in pedidos:
        chave = pedido['client_id']
        if chave not in total_por_id:
            total_por_id[chave] = 0
        total_por_id[chave] += pedido['valor']
    
    lista_nova = [{'nome': clientes_por_id[id_cliente], 'total': valor}
                  for id_cliente, valor in total_por_id.items()]
    
    lista_ordenada = sorted(lista_nova, key=lambda item: item['total'], reverse=True)
    
    return lista_ordenada
    
print(pedidos_por_cliente(clientes, pedidos))