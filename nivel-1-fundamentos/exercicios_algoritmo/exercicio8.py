pedidos = [
    {"cliente": "Ana", "itens": [("pizza", 45.00), ("refrigerante", 8.00)]},
    {"cliente": "Bruno", "itens": [("hambúrguer", 28.00), ("batata", 15.00), ("suco", 10.00)]},
    {"cliente": "Clara", "itens": [("salada", 22.00)]},
    {"cliente": "Diego", "itens": [("pizza", 45.00), ("pizza", 45.00), ("refrigerante", 8.00)]},
    {"cliente": "Elis", "itens": [("hambúrguer", 28.00), ("suco", 10.00)]},
]

"""
FUNÇÃO: soma_total_cliente
FAZ: soma total de gastos do cliente do maior para o menor.
ENTRADA: lista pedidos de dicionários com chave 'cliente' (str) e 'itens' (lista de tuplas (str, float))
SAÍDA: lista de tuplas (clientes, soma de gastos) ordenada do maior para o menor.
REGRA:
Cada cliente pode fazer um ou mais pedidos. A função tem que somar todos esses gastos para cada cliente e depois apresentar
uma lista com todos os clientes ordenando-os do que mais gastou para o que menos gastou.
EXCEÇÃO: não tem. o exercício não tem entrada de usuário.
"""
def soma_total_cliente(pedidos):
    clientes_soma = []
    for pedido in pedidos:
        cliente = pedido["cliente"]
        soma = 0
        for item in pedido["itens"]:
            soma += item[1]
        clientes_soma.append((cliente, soma))
        
    print(sorted(clientes_soma, key=lambda cliente: cliente[1], reverse=True))


soma_total_cliente(pedidos)

"""
FUNÇÃO: itens_distintos_vendidos
FAZ: mostra todos os itens distintos pedidos na noite em ordem alfabética
ENTRADA: lista pedidos de dicionários com chave 'cliente' (str) e 'itens' (lista de tuplas (str, float))
SAÍDA: lista de itens (str) distintos pedidos em ordem alfabetica.
REGRA:
Cada pedido pode ter um ou mais itens. a função deve discriminar todos os itens e retirar os itens repetidos. Depois deve apresenta-los ao usuario
em ordem alfabetica.
EXCEÇÃO: não há. Função recebe estrutura fixa do exercício, sem entrada externa.
"""

def itens_distintos_vendidos(pedidos):
    lista_itens = []
    
    for pedido in pedidos:
        for item in pedido["itens"]:
            lista_itens.append(item[0])
    
    conjunto_itens = set(lista_itens)
    lista_ordenada = sorted(conjunto_itens)
    print(lista_ordenada)
    
itens_distintos_vendidos(pedidos)