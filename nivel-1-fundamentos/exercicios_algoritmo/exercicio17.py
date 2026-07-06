vendas = [
    {"produto": "caneta",   "categoria": "papelaria",  "valor": 5.50,  "quantidade": 3},
    {"produto": "caderno",  "categoria": "papelaria",  "valor": 25.00, "quantidade": 2},
    {"produto": "mouse",    "categoria": "eletronico", "valor": 80.00, "quantidade": 1},
    {"produto": "teclado",  "categoria": "eletronico", "valor": 150.00,"quantidade": 2},
    {"produto": "lapis",    "categoria": "papelaria",  "valor": 2.00,  "quantidade": 10},
    {"produto": "fone",     "categoria": "eletronico", "valor": 200.00,"quantidade": 1},
    {"produto": "borracha", "categoria": "papelaria",  "valor": 1.50,  "quantidade": 5},
    {"produto": "monitor",  "categoria": "eletronico", "valor": 900.00,"quantidade": 1},
]

"""
Quero o faturamento total por categoria, considerando apenas vendas cuja linha (valor × quantidade) seja de no mínimo R$ 10,00. Ordenado do maior faturamento pro menor.
"""

""" MODELAGEM:
FAZ: recebe uma lista de dicionários e devolve uma lista de dicionários contendo categoria e faturamento (valor x quantidade, apenas para itens que tenham faturamento unitário igual
ou maior a 10). Ordena os dicionários por faturamento (maior para menor)
ENTRADA: lista venda (dict) com chaves produto (str), categoria (str), valor (float), quantidade (int)
SAÍDA: lista categoria_faturamento_ordenada (dict) com duas chaves, categoria (sstr) e faturamento (float). ordenada por faturamento do maior para o menor.
REGRA: a função recebe a lista vendas (dict) como argumento, calcula o faturamento de cada linha (valor x quantidade), filtra (retira) os dicionários cujo faturamento é menor que 10.0,
agrupa por categoria e retorna com uma lista categoria_faturamento_ordenada (dict) por categoria e faturamento. ordenada pelo faturamento, do maior para o menor.
EXCEÇÃO: Não há exceção, pois o enunciado garante que as listas vêm bem formadas; vendas com linha < 10 não são erro, são filtradas (filtro implícito).
 """
 
""" MULTI-STEP DECOMPOSITION:
Bloco 1 - list comprehension: filtra itens cujo faturamento seja menor que 10.
Bloco 2 - dict-acumulator: fazer o agrupamento das chaves categoria e faturamento.
Bloco 3 - construção da lista: constrói a nova lista de dicionários com as chaves categoria e quantidade.
Bloco 4 - ordenação: ordena a nova lista criada e agrupada pela chave faturamento, do maior para o menor.saída: 
"""
def faturamento_das_categorias(vendas):
    lista_filtrada = [venda for venda in vendas if venda["valor"] * venda["quantidade"] >= 10]
    
    faturamento = {}
    for venda in lista_filtrada:
        chave = venda["categoria"]
        valor = venda["valor"] * venda["quantidade"]
        if chave not in faturamento:
            faturamento[chave] = 0
        faturamento[chave] += valor
        
    nova_lista = []
    for chave, valor in faturamento.items():
        nova_lista.append({"categoria": chave, "faturamento": valor})
    
    ordenada = sorted(nova_lista, key=lambda item: item["faturamento"], reverse=True)
    
    return ordenada

print(faturamento_das_categorias(vendas))