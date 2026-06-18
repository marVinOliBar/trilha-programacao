"""
OBJETIVO: mostrar a lista ordenada pelo preço, do mais barato pro mais caro.
ENTRA: lista produto com tuplas
SAI: lista de tuplas ordenadas pelo preço
REGRA:
. ordenar a lista
. imprimir a lista ordenada
"""

produtos = [
    ("arroz", 22.90),
    ("feijão", 8.50),
    ("café", 18.75),
    ("leite", 6.40),
    ("pão", 12.00),
]

print(sorted(produtos, key=lambda produto: produto[1]))