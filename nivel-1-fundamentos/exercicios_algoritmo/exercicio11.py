horas_extras = [
    {"funcionario": "Ana", "depto": "TI", "data": "2026-06-03", "horas": 2.5, "aprovada": True},
    {"funcionario": "Bruno", "depto": "RH", "data": "2026-06-05", "horas": 1.5, "aprovada": True},
    {"funcionario": "Ana", "depto": "TI", "data": "2026-06-10", "horas": 3.0, "aprovada": False},
    {"funcionario": "Clara", "depto": "TI", "data": "2026-06-12", "horas": 4.0, "aprovada": True},
    {"funcionario": "Bruno", "depto": "RH", "data": "2026-06-15", "horas": 2.0, "aprovada": True},
    {"funcionario": "Ana", "depto": "TI", "data": "2026-06-18", "horas": 1.5, "aprovada": True},
    {"funcionario": "Diego", "depto": "Vendas", "data": "2026-06-20", "horas": 5.0, "aprovada": True},
    {"funcionario": "Clara", "depto": "TI", "data": "2026-06-22", "horas": 2.0, "aprovada": False},
    {"funcionario": "Diego", "depto": "Vendas", "data": "2026-06-25", "horas": 3.5, "aprovada": True},
]

"""horas_aprovadas_por_funcionario — devolve uma lista de tuplas (funcionario, depto, total_horas) considerando somente horas extras aprovadas, ordenada por:

Total de horas (decrescente — quem fez mais horas primeiro)
Empate: nome do funcionário (alfabético)
"""

"""
FUNÇÃO: horas_aprovadas_por_funcionario
FAZ: recebe uma lista de dicionários e devolve uma lista de tuplas com o valor da chave "aprovada" igual a True.
ENTRADA: lista de dicionários com chaves 'funcionario' (str), 'depto' (str), 'data' (str), 'horas' (float), 'aprovada' (bool)
SAÍDA: lista de tuplas (funcionario (str), depto (str), total_horas (float)) ordenadas por total_horas em ordem decrescente e funcionario alfabeticamente
REGRA:
. a função recebe a lista, separa os dicionários cujo valor da chave "aprovada" são True, posteriormente faz o agrupamento dos valores da chaves escolhidas em dicionário. as chaves funcionario
e depto são inseridas no dicionário juntas com formato de tupla. Faz a ordenação
segundo o critério por total_horas em ordem decrescente e por funcionarios em ordem alfabética. imprime o resultado para o usuário.
EXCEÇÃO: não tem, pois não há entrada
"""
def horas_aprovadas_por_funcionario(horas_extras):
    horas_aprovadas = []
    for extra in horas_extras:
        if extra["aprovada"]:
            horas_aprovadas.append(extra)
    
    funcionarios = {}
    for aprovadas in horas_aprovadas:
        chave = (aprovadas["funcionario"], aprovadas["depto"])
        if chave not in funcionarios:
            funcionarios[chave] = 0
        funcionarios[chave] += aprovadas["horas"]
        
    ordenado = sorted(funcionarios.items(), key=lambda l: (-l[1], l[0]))
    final = []
    for chave, horas in ordenado:
        funcionario, depto = chave
        final.append((funcionario, depto, horas))
        
    print(final)

horas_aprovadas_por_funcionario(horas_extras)