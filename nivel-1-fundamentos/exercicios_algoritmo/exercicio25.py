# SELECT sgb, tipo, duracao_min, status FROM ocorrencia
linhas = [
    ("1º SGB", "incendio", 45, "encerrada"),
    ("1º SGB", "resgate",  30, "encerrada"),
    ("2º SGB", "incendio", 60, "encerrada"),
    ("1º SGB", "incendio", 75, "encerrada"),
    ("2º SGB", "resgate",  20, "em andamento"),
    ("1º SGB", "resgate",  50, "encerrada"),
    ("3º SGB", "incendio", 90, "encerrada"),
    ("2º SGB", "incendio", 40, "encerrada"),
    ("1º SGB", "incendio", 30, "encerrada"),
    ("3º SGB", "resgate",  25, "cancelada"),
    ("2º SGB", "incendio", 50, "encerrada"),
    ("1º SGB", "resgate",  40, "encerrada"),
]

"""
Problema: considerando apenas as ocorrências encerradas, produzir, para cada par (sgb, tipo), a quantidade de ocorrências e a duração média em minutos. Ordenar por quantidade (maior primeiro); empate resolve por sgb em ordem alfabética; empate persistente resolve por tipo em ordem alfabética.

Saída: lista de tuplas (sgb, tipo, quantidade, media), com a média em uma casa decimal.

Antes de codar, me manda a modelagem — um bloco nomeado por operação, no molde 

FAZ: recebe como argumento uma lista de tuplas, filtra as ocorrencias encerradas, depois agrupa as tuplas por sgb + tipo, conta quantas ocorrencias tiveram com essas caracterísitcas e calcula a media, em minutos, da duração de cada ocorrência. retorna uma lista de tuplas com esses dados: sgb, tipo, quantidade e média.
ENTRADA: lista 'linhas' de tuplas com índices 0 (sgb), 1 (tipo), 2 (duração em minutos), 3 (estado)
SAÍDA: lista de tuplas com os índices 0 (sgb), 1 (tipo), 2 (quantidade), 3 (media)
REGRA:
BLOCO 1 - Filter
    cria variavel 'ocorrencias_encerradas' e atribui a ela uma lista de tuplas com indices 'sgb', 'tipo' e 'tempo' para cada encerrada em ocorrencias, se encerrada na posição 3 é igual a 'encerrada'.

BLOCO 2 - GROUP by
    cria a variavel 'contador' e atribui a ela dicionário vazio
    cria a variavel 'soma' e atribui a ela dicionário vazio
    percorre para cada 'sgb', 'tipo', 'tempo' na lista 'ocorrencias_encerradas'.
        cria a variavel 'chave' e atribui a ela 'sgb' e 'tipo'
        verificar se chave não está em 'contador': 
            se sim
                atribuir 'contador'[chave] 0
                atribuir 'soma'[chave] 0
        'contador'[chave] incrementa 1
        'soma'[chave] incrementa 'tempo'
        
BLOCO 3 - MAP
    cria a variavel lista_agrupada atribui a ela lista vazia
    percorrer para chave, valor em contador.items()
        sgb, tipo = chave
        media recebe o resultado da divisão de soma[chave] dividido por valor
        lista_agrupada acrescenta (sgb, tipo, valor, media)
    
BLOCO 4 - SORT
    cria a variavel lista_ordenada e atribui a ela a função sorted ordenando a lista_com_media, no índice 2 invertido, indice 0 normal, e no índice 1 normal
    
    retorna a lista_ordenada
"""

def qtde_e_tempo_ocorrencias(linhas):
    ocorrencias_encerradas = [(ocorrencia[0], ocorrencia[1], ocorrencia[2]) for ocorrencia in linhas if ocorrencia[3] == 'encerrada']
    
    contador = {}
    soma = {}
    for sgb, tipo, tempo in ocorrencias_encerradas:
        chave = (sgb, tipo)
        if chave not in contador:
            contador[chave] = 0
            soma[chave] = 0
        contador[chave] += 1
        soma[chave] += tempo
    
    lista_agrupada = []
    for chave, valor in contador.items():
        sgb, tipo = chave
        media = soma[chave] / valor
        lista_agrupada.append((sgb, tipo, valor, round(media, 1)))
        
    lista_ordenada = sorted(lista_agrupada, key=lambda indice: (-indice[2], indice[0], indice[1]))
    
    return lista_ordenada
    
    
print(qtde_e_tempo_ocorrencias(linhas))
