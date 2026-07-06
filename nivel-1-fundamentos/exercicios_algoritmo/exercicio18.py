""" FUNÇÃO: tickets_por_prioridade_alta
FAZ: recebe a lista tickets com dicionários, filtra a lista tickets, agrupa os dados de prioridade por cliente, constroi uma nova lista de dicionários, ordena a nova lista
e devolve uma lista de dicionários
ENTRADA: lista tickets com (dicts) e chaves id (int), cliente (str), prioridade (str), horas_aberto (int)
SAÍDA: lista tickets_filtrados com (dicts) e chaves cliente (str), tickets_criticos (int)
REGRA: a função recebe a lista tickets como argumento,
    Bloco 1 - Filter
    . declarar uma variavel e atribuir a ela o resultado do filtro para prioridade alta e mais de 6 horas em aberto.
    Bloco 2 - Agrupamento
    . declara uma variável contador e atribui dicionario vazio a ela
    . percorre a lista filtrada e atribui o valor da chave 'cliente' a variável chave.
    . verifica se chave NÃO está dentro do dicionário contador
    ..se sim, adiciona o valor zero ao dicionário com a chave
    . adiciona o valor 1 ao dicionario com a chave
    Bloco 3 - Map
    . declara nova variavel e atribui uma list comprehension construindo dicionários com as chaves 'cliente' (str) e 'tickets_criticos' (int) atribuindo a elas os valores obtidos
    do agrupamento.
    Bloco 4 - Sort
    . ordena a nova lista de dicionarios pela quantidade de tickets abertos, em ordem decrescente.
    Bloco 5
    . retorna com o valor da lista_ordenada. 
EXCEÇÕES: Não há exceção — o enunciado garante que a lista vem bem formada; tickets que não passam nos filtros não são erro, são filtro implícito. """


tickets = [
    {"id": 101, "cliente": "acme",     "prioridade": "alta",   "horas_aberto": 12},
    {"id": 102, "cliente": "globex",   "prioridade": "baixa",  "horas_aberto": 48},
    {"id": 103, "cliente": "acme",     "prioridade": "alta",   "horas_aberto": 3},
    {"id": 104, "cliente": "initech",  "prioridade": "media",  "horas_aberto": 30},
    {"id": 105, "cliente": "globex",   "prioridade": "alta",   "horas_aberto": 8},
    {"id": 106, "cliente": "acme",     "prioridade": "media",  "horas_aberto": 5},
    {"id": 107, "cliente": "initech",  "prioridade": "alta",   "horas_aberto": 20},
    {"id": 108, "cliente": "globex",   "prioridade": "alta",   "horas_aberto": 1},
]

# Quero saber quantos tickets de prioridade alta cada cliente tem em aberto há mais de 6 horas. Ordenado do cliente com mais tickets críticos pro com menos.

def tickets_por_prioridade_alta(tickets):
    filtro_prioridadealta_maisdeseishoras = [t for t in tickets if t['prioridade'] == 'alta' and t['horas_aberto'] > 6]
    
    contador = {}
    for ticket in filtro_prioridadealta_maisdeseishoras:
        chave = ticket['cliente']
        if chave not in contador:
            contador[chave] = 0
        contador[chave] += 1
    
    lista_dicionarios = [{'cliente': nome, 'tickets_criticos': quantidade} for nome, quantidade in contador.items()]
    
    tickets_filtrados = sorted(lista_dicionarios, key=lambda d: -d['tickets_criticos'])
    
    return tickets_filtrados

print(tickets_por_prioridade_alta(tickets))