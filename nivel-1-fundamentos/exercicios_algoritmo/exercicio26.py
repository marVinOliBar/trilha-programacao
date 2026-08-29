# SELECT posto, equipe, viatura, duracao_min, status FROM empenho
linhas = [
    ("Posto Central", "amarela", "ABT-01", 95, "atendida"),
    ("Posto Central", "azul",    "ABT-02", 40, "atendida"),
    ("Posto Norte",   "amarela", "AR-11",  70, "atendida"),
    ("Posto Central", "amarela", "ASE-03", 55, "atendida"),
    ("Posto Norte",   "verde",   "AR-11",  30, "cancelada"),
    ("Posto Central", "azul",    "ABT-02", 80, "atendida"),
    ("Posto Sul",     "verde",   "ABT-07", 75, "atendida"),
    ("Posto Norte",   "amarela", "AR-12", 110, "atendida"),
    ("Posto Central", "amarela", "ABT-01", 25, "atendida"),
    ("Posto Sul",     "verde",   "ABT-07", 45, "em andamento"),
    ("Posto Norte",   "verde",   "AR-11",  90, "atendida"),
    ("Posto Sul",     "amarela", "ASE-09", 35, "atendida"),
    ("Posto Central", "azul",    "ABT-05", 30, "atendida"),
    ("Posto Norte",   "amarela", "AR-12",  20, "atendida"),
    ("Posto Sul",     "verde",   "ABT-07", 75, "atendida"),
]
"""
Problema: considerando apenas os empenhos atendidos, produzir para cada par (posto, equipe): quantos empenhos, o total de minutos e a maior duração individual do grupo.

Saída: lista de tuplas (posto, equipe, quantidade, total_min, maior_min). Ordenar por total de minutos decrescente; empate por posto crescente; empate persistente por equipe crescente.

O que muda em relação ao ex25: a entrada tem cinco campos e um deles (viatura) não serve pra nada — você desempacota cinco e usa quatro. E há um terceiro acumulador que não incrementa.

Modelagem na régua nova: Filter, Group by, Map e Sort em forma curta — uma linha cada, nome do padrão e o verbo. Só o acumulador de máximo pede o molde, e nele a linha que me interessa é a inicialização: com que valor ele nasce, e por quê.

REGRA:
O primeiro é um Filter eu percorro a lista e mantenho somente as ocorrencias com o estado 'atendida'; O segundo é um Group by misto para o par posto, equipe: será um group by count onde somarei a quantidade de ocorrência para cada par posto equipe, um group by sum, onde eu somarei todos os minutos para as ocorrencias do posto, equipe e também um group by max onde eu verificarei o tempo máximo de atendimento de ocorrência para cada posto, equipe - para isso eu assumo que o primeiro valor da variável 'maximo' que irei utilizar para comparar, seja igual ao valor do primeiro item do grupo e não corro o risco de dimensionar aleatoriamente e perder um valor qualquer. O próximo passo é um Map para transformar os três dicionários que foram criados em uma lista de tuplas. Por último um Sort que irá ordenar a lista primeiro pelo total de minutos em ordem decrescente, em caso de empate organizo por posto em ordem alfabética e em caso de empate organizo por equipe em ordem alfabética.
"""
def maior_tempo_ocorrencia(linhas):
    filtro = [ocorrencia for ocorrencia in linhas if ocorrencia[4] == 'atendida']
    
    soma = {}
    contador = {}
    maximo = {}
    for posto, equipe, _, tempo, _ in filtro:
        chave = (posto, equipe)
        if chave not in contador:
            contador[chave] = 0
            soma[chave] = 0
            maximo[chave] = tempo
        contador[chave] += 1
        soma[chave] += tempo
        if maximo[chave] < tempo:
            maximo[chave] = tempo
        
    lista_agrupada = []
    for chave, quantidade in contador.items():
        posto, equipe = chave
        quantidade = quantidade
        total_min = soma[chave]
        max_min = maximo[chave]
        lista_agrupada.append((posto, equipe, quantidade, total_min, max_min))
    
    lista_ordenada = sorted(lista_agrupada, key=lambda ocorrencia: (-ocorrencia[3], ocorrencia[0], ocorrencia[1]))
    
    return lista_ordenada

print(maior_tempo_ocorrencia(linhas))