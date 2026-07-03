vendas = [
    {"vendedor": "Ana", "categoria": "celular", "valor": 1800.00},
    {"vendedor": "Bruno", "categoria": "notebook", "valor": 3500.00},
    {"vendedor": "Ana", "categoria": "celular", "valor": 2200.00},
    {"vendedor": "Clara", "categoria": "tablet", "valor": 1200.00},
    {"vendedor": "Bruno", "categoria": "notebook", "valor": 4100.00},
    {"vendedor": "Ana", "categoria": "tablet", "valor": 950.00},
    {"vendedor": "Diego", "categoria": "celular", "valor": 1500.00},
    {"vendedor": "Clara", "categoria": "notebook", "valor": 3800.00},
    {"vendedor": "Diego", "categoria": "celular", "valor": 2100.00},
    {"vendedor": "Bruno", "categoria": "tablet", "valor": 1100.00},
]

"""

A ideia: em vez de contador e ticket_total separados, use um único dict onde cada chave (vendedor) tem como valor outro dict com soma e contagem:

stats = {
    "Ana": {"soma": 4950.0, "contagem": 3},
    "Bruno": {"soma": 8700.0, "contagem": 3},
    ...
}

"""
def ticket_medio_por_vendedor(vendas):
    ticket_medio = {}
    for venda in vendas:
        chave = venda["vendedor"]
        if chave not in ticket_medio:
            ticket_medio[chave] = {"soma": 0, "contagem": 0}
        ticket_medio[chave]["soma"] += venda["valor"]
        ticket_medio[chave]["contagem"] += 1
        
    lista_ticket_medio = []
    for vendedor in ticket_medio:
       lista_ticket_medio.append((vendedor, ticket_medio[vendedor]["soma"] / ticket_medio[vendedor]["contagem"]))

    ticket_ordenado = sorted(lista_ticket_medio, key=lambda t: (-t[1], t[0]))
    print(ticket_ordenado)

ticket_medio_por_vendedor(vendas)
"""
Função: ticket_medio_por_vendedor
Faz: devolve lista de tuplas (vendedor, ticket_medio) — o ticket médio é o valor médio das vendas que o vendedor fez. Ordenada por ticket médio decrescente, empate alfabético.
Entrada: lista vendas com dicionários (vendedor: str, categoria: str, valor, float)
Saída: lista tuplas (vendedor: str, ticket_medio: float) ordenada por ticket medio decrescente e vendedor alfabetico
Regra:
. A função recebe a lista de dicionários, soma os valores de vendas de cada vendedor, conta quantas vendas fez, faz a media. Retorna a tupla com o nome do vendedor e o ticket_medio
produzido.
Exceção: Não tem entrada. Sem exceção.
"""