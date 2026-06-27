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
Função: ticket_medio_por_vendedor
Faz: devolve lista de tuplas (vendedor, ticket_medio) — o ticket médio é o valor médio das vendas que o vendedor fez. Ordenada por ticket médio decrescente, empate alfabético.
Entrada: lista vendas com dicionários (vendedor: str, categoria: str, valor, float)
Saída: lista tuplas (vendedor: str, ticket_medio: float) ordenada por ticket medio decrescente e vendedor alfabetico
Regra:
. A função recebe a lista de dicionários, soma os valores de vendas de cada vendedor, conta quantas vendas fez, faz a ticket_medio. Retorna a tupla com o nome do vendedor e o ticket_medio
produzido.
Exceção: Não tem entrada. Sem exceção.
"""

def ticket_medio_por_vendedor(vendas):
    contador = {}
    ticket_total = {}
    
    for venda in vendas:
        chave = venda["vendedor"]
        if chave not in contador:
            contador[chave] = 0
        contador[chave] += 1
        if chave not in ticket_total:
            ticket_total[chave] = 0
        ticket_total[chave] += venda["valor"]
    
    ticket_medio = []
    for vendedor in contador:
        ticket_medio.append((vendedor, ticket_total[vendedor] / contador[vendedor]))
    
    
    ticket_ordenado = sorted(ticket_medio, key=lambda t: (-t[1], t[0]))
    print(ticket_ordenado)
    
    
ticket_medio_por_vendedor(vendas)