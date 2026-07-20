vendas = [
    {"produto": "caneta",   "categoria": "papelaria",  "mes": "jan", "valor": 15.00},
    {"produto": "mouse",    "categoria": "eletronico", "mes": "jan", "valor": 80.00},
    {"produto": "caderno",  "categoria": "papelaria",  "mes": "fev", "valor": 25.00},
    {"produto": "teclado",  "categoria": "eletronico", "mes": "jan", "valor": 150.00},
    {"produto": "lapis",    "categoria": "papelaria",  "mes": "jan", "valor": 5.00},
    {"produto": "fone",     "categoria": "eletronico", "mes": "fev", "valor": 200.00},
    {"produto": "borracha", "categoria": "papelaria",  "mes": "fev", "valor": 3.00},
    {"produto": "monitor",  "categoria": "eletronico", "mes": "jan", "valor": 900.00},
    {"produto": "regua",    "categoria": "papelaria",  "mes": "jan", "valor": 8.00},
]
"""
Objetivo: Faturamento total por combinação categoria+mês, ordenado do maior pro menor.
Saída esperada:

[
    {"categoria": "eletronico", "mes": "jan", "total": 1130.00},
    {"categoria": "eletronico", "mes": "fev", "total": 200.00},
    {"categoria": "papelaria",  "mes": "jan", "total": 28.00},
    {"categoria": "papelaria",  "mes": "fev", "total": 28.00},
]

FAZ: recebe a lista de dicionários vendas, e faz o agrupamento por categoria e mês para ver o total de cada um. 
ENTRADA: lista de dicionários vendas com as chaves 'produto' (str), 'categoria' (str), 'mes' (str) e 'valor' (float).
SAÍDA: lista de diconários faturamento com as chaves 'categoria' (str), 'mes' (str) e 'total' (float).
REGRA:
BLOCO 1 - GROUP BY SUM
    declarar variável acumulador e atribuir a ela um dicionário vazio.
    percorrer a lista vendas para cada dicionário de venda.
        criar variavel chave e atribuir a tupla 'categoria' e 'mes'
        verificar se chave não existe em acumulador
            se sim, a chave em acumulador recebe 0
        incrementar 'valor' de venda na chave em acumulador.
BLOCO 2 - MAP
    criar variavel lista_de_valores e atribuir a ela uma list comprehension para a chave do dicionário desempacotada e o valor do dicionário do acumulador.items() e formando dicionarios
com as chaves 'categoria', 'mes' e 'total'.
BLOCO 3 - SORT
    ordenar a lista pela chave 'total', do maior para o menor, e ordem alfabética de mês e atribuir a variavel lista_ordenada
    retornar lista_ordenada.
"""

def faturamento_total(vendas):
    acumulador = {}
    for venda in vendas:
        chave = (venda['categoria'], venda['mes'])
        if chave not in acumulador:
            acumulador[chave] = 0
        acumulador[chave] += venda['valor']
        
    lista_de_valores = [{'categoria': categoria, 'mes': mes, 'total': total}for (categoria, mes), total in acumulador.items()]
    lista_ordenada = sorted(lista_de_valores, key=lambda item: (-item['total'], item['mes']))
    
    return lista_ordenada        
    
print(faturamento_total(vendas))