"""
Objetivo:
. Mostrar a lista de alunos únicos que passaram pela sala (sem repetir).
. Mostrar essa lista em ordem alfabética.
Entra: lista entradas
Sai: lista de alunos em ordem alfabética e sem repetição
Regra:
. primeiro transformar a lista em conjunto para excluir os repetidos
. apresentar o conjunto em ordem alfabetica"""

entradas = ["Ana", "Bruno", "Clara", "Ana", "Diego", "Bruno", "Ana", "Elis"]

alunos = set(entradas)

print(sorted(alunos))