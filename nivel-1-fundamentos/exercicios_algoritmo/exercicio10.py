atendimentos = [
    {"prefixo": "ABT-101", "tipo": "incêndio", "duracao_min": 45},
    {"prefixo": "UR-201", "tipo": "resgate", "duracao_min": 80},
    {"prefixo": "ABT-101", "tipo": "incêndio", "duracao_min": 30},
    {"prefixo": "UR-201", "tipo": "transporte", "duracao_min": 25},
    {"prefixo": "ABT-103", "tipo": "incêndio", "duracao_min": 60},
    {"prefixo": "UR-201", "tipo": "resgate", "duracao_min": 95},
    {"prefixo": "ABT-101", "tipo": "vazamento", "duracao_min": 20},
    {"prefixo": "ABT-103", "tipo": "incêndio", "duracao_min": 50},
]

# total_minutos_por_viatura — devolve uma lista de tuplas (prefixo, total_minutos), ordenada do que mais trabalhou pro que menos trabalhou.
"""FUNÇÃO: total_minutos_por_viatura
FAZ: recebe uma lista de dicionários e devolve uma lista de tuplas ordenada sobre o tempo de trabalho, do maior para o menor.
ENTRADA: lista de dicionários com chaves 'prefixo' (str), 'tipo' (str), 'duracao_min' (int)
SAÍDA: lista (list) de tuplas (tuple) contendo o prefixo da viatura e o total de minutos que ela trabalhou.
REGRA:
. a função recebe a lista de dicionários, separa os prefixos e os minutos trabalhados em cada atendimento. após somar os minutos de cada viatura, apresenta o prefixo e os minutos trabalhados
por cada viatura, ordenando de acordo com os minutos trabalhados, do maior para o menor.
EXCEÇÃO: não há, pois não há entradas."""
def minutos_por_viatura(atendimentos):
    prefixos_e_tempo = {}
    for atendimento in atendimentos:
        chave = atendimento["prefixo"]
        if chave not in prefixos_e_tempo:
            prefixos_e_tempo[chave] = 0
        prefixos_e_tempo[chave] += atendimento['duracao_min']
        
    lista_viaturas = list(prefixos_e_tempo.items())
    ordenado = sorted(lista_viaturas, key=lambda t: (-t[1], t[0]))
    print(ordenado)

#minutos_por_viatura(atendimentos)


# contagem_por_tipo — devolve uma lista de tuplas (tipo, quantidade), ordenada por quantidade decrescente; em caso de empate, tipo alfabético.
"""FUNÇÃO: contagem_por_tipo
FAZ: recebe uma lista de dicionários e devolve uma lista de tuplas ordenada pela quantidade de atendimentos e depois por tipo alfabético.
ENTRADA: lista de dicionários com chaves 'prefixo' (str), 'tipo' (str), 'duracao_min' (int)
SAÍDA: lista (list) de tuplas (tuple) contendo o tipo de ocorrencia e a quantidade de ocorrências ordenada pela quantidade decrescente e alfabético para tipo.
REGRA:
. a função recebe a lista de dicionários, separa os tipos de ocorrências atendidas e depois faz uma contagem para cada tipo específico. depois apresenta uma tupla com os tipos e a quantidade 
de ocorrencias atendidas.
EXCEÇÃO: não há, pois não há entradas."""
def contagem_por_tipo(atendimentos):
    tipo = {}
    for atendimento in atendimentos:
        chave = atendimento["tipo"]
        if chave not in tipo:
            tipo[chave] = 0
        tipo[chave] += 1
        
    lista_tipo = list(tipo.items())
    ordenado = sorted(lista_tipo, key=lambda t: (-t[1], t[0]))
    print(ordenado)
    
contagem_por_tipo(atendimentos)