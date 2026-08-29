# SELECT viatura, data, natureza FROM ocorrencia
registros = [
    ("ABT-01", "2026-08-03", "incendio_estrutural"),
    ("AR-11",  "2026-08-03", "salvamento_altura"),
    ("ABT-01", "2026-08-05", "incendio_vegetacao"),
    ("ASE-03", "2026-08-05", "atendimento_pre_hospitalar"),
    ("ABT-01", "2026-08-09", "incendio_estrutural"),
    ("AR-11",  "2026-08-11", "salvamento_altura"),
    ("ABT-07", "2026-08-12", "incendio_vegetacao"),
    ("AR-11",  "2026-08-12", "produto_perigoso"),
    ("ASE-03", "2026-08-14", "atendimento_pre_hospitalar"),
    ("ABT-01", "2026-08-15", "incendio_estrutural"),
    ("ABT-07", "2026-08-16", "salvamento_aquatico"),
    ("AR-11",  "2026-08-18", "salvamento_altura"),
]

"""
Problema: para cada viatura, quantas naturezas distintas ela atendeu e quais são elas.

Saída: lista de tuplas (viatura, quantidade_de_naturezas, lista_de_naturezas_ordenada). Ordenar por quantidade decrescente; empate por prefixo da viatura em ordem alfabética.

O campo data não serve pra nada aqui.

Modelagem em forma curta — uma linha por bloco. E antes de rodar, conta à mão: quantas naturezas distintas a AR-11 atendeu? Escreve o número antes de deixar o computador te responder.

regra:
Group by em coleção: para cada viatura, acumula as naturezas num set.
Map: percorre o acumulador e monta (viatura, tamanho do set, set ordenado como lista).
Sort: quantidade decrescente, viatura crescente no desempate.
"""

def naturezas_por_viatura(registros):
    resultado = {}
    for viatura, _, natureza in registros:
        if viatura not in resultado:
            resultado[viatura] = set()
        resultado[viatura].add(natureza)
    
    lista_agrupada = []
    for viatura, naturezas in resultado.items():
        quantidade_de_naturezas = len(naturezas)
        naturezas_ordenadas = sorted(naturezas)
        lista_agrupada.append((viatura, quantidade_de_naturezas, naturezas_ordenadas))
        
    lista_ordenada = sorted(lista_agrupada, key=lambda x: (-x[1], x[0]))
        
    
    return lista_ordenada
print(naturezas_por_viatura(registros))
