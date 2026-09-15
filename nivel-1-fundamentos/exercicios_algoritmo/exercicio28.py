viaturas = [
    ("abt-01", "eb vila uniao"),
    ("abt-03", "sul"),
    ("ur-13107", "sul"),
]

atendimentos = [
    ("abt-01", 7),
    ("ur-13107", 7),
    ("abt-03", 12),
]

"""
Escreve uma função que devolve, para cada atendimento, a ocorrência, o prefixo e a estação daquela viatura.

Saída esperada:

python
[(7, "abt-01", "eb vila uniao"),
 (7, "ur-13107", "sul"),
 (12, "abt-03", "sul")]

Sem ordenar, sem agrupar, sem filtrar. Só o cruzamento.
"""

def cruzamento(viaturas, atendimentos):
    posto_por_viatura = {prefixo:posto for prefixo, posto in viaturas}
        
    resultado = []
    for prefixo, id_ocorrencia in atendimentos:
        posto = posto_por_viatura[prefixo]
        resultado.append((id_ocorrencia, prefixo, posto))
    
    return cruzamento
    

print(cruzamento(viaturas, atendimentos))