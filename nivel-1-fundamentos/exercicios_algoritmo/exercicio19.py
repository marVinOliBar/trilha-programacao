commits = [
    {"author": "ana",   "timestamp": "2026-07-06 09:15"},  # segunda
    {"author": "bruno", "timestamp": "2026-07-06 14:20"},  # segunda
    {"author": "ana",   "timestamp": "2026-07-07 10:00"},  # terça
    {"author": "carla", "timestamp": "2026-07-04 22:45"},  # sábado
    {"author": "ana",   "timestamp": "2026-07-06 18:30"},  # segunda
    {"author": "bruno", "timestamp": "2026-07-05 11:00"},  # domingo
    {"author": "carla", "timestamp": "2026-07-07 16:15"},  # terça
]

"""
Saída Esperada:
[
    {"dia_semana": "segunda", "commits": 3},
    {"dia_semana": "terça",   "commits": 2},
    {"dia_semana": "sábado",  "commits": 1},
    {"dia_semana": "domingo", "commits": 1},
]

Problema: Você tem uma lista de commits com autor e timestamp. Devolva uma lista de dicts com cada dia da semana e o total de commits feitos naquele dia,
ordenada do dia com mais commits pro com menos.

FAZ: recebe lista commits de dicionários com chaves 'author' (str) e 'timestamp' (str), transforma o formato das datas para dias da semana e depois os agrupa por contagem de quantos
commits foram efetuados naquele dia. devolve lista de dicionarios com as chaves 'dia_semana' (str) e 'commits' (int)
ENTRADA: lista commits com dicionários com chaves 'author' (str) e 'timestamp' (str)
SAÍDA: lista com dicionarios de chaves 'dia_semana' (str) e 'commits' (int)
REGRA:

BLOCO 1 - MAP
    função recebe a lista commits como argumento
    declara uma variável e atribui a ela uma lista modificada da lista commits, com chaves 'author' (str) e 'dia_semana' (str)

BLOCO 2 - GROUP BY COUNT
    declara variavel contador e atribui a ele um dicionario vazio
    percorre a lista commits com a variavel commit
        declara variavel chave e atribui a ela o valor da chave 'dia_semana'
        verifica se não há valor da variavel chave dentro do dicionario contador
            se sim, atribui a variavel chave do dicionario contador o valor 0
        soma + 1 a variavel chave do dicionario contador

BLOCO 3 - MAP (.items())
    declara variavel lista_inicial e atribui a ela uma lista de dicionários com as chaves 'dia_semana' (str), com a chave do dicionario contador, e 'commits' (int), com o valor do
dicionario do contador. Usando list comprehension

BLOCO 4 - SORT
    declara variavel lista_ordenada e atribui a ela a ordenação da lista_inicial pelos valores da chave 'commits', do maior para o menor.
    
BLOCO 5 - return
    retorna a variavel lista_ordenada
        
"""
from datetime import datetime

def dias_semana(commits):
    indice_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    novo_commits = []
    for commit in commits:
        objeto_data = datetime.fromisoformat(commit['timestamp'])
        dia = indice_semana[objeto_data.weekday()]
        novo_commits.append({'author': commit['author'], 'dia_semana': dia})
    
    return novo_commits


def commits_por_dia_semana(commits):
    
    novo_commits = dias_semana(commits)
    
    contador = {}
    for commit in novo_commits:
        chave = commit['dia_semana']
        if chave not in contador:
            contador[chave] = 0
        contador[chave] += 1
    
    lista_inicial = [{'dia_semana': dia, 'commits': qtd_commits} for dia, qtd_commits in contador.items()]
    
    lista_ordenada = sorted(lista_inicial, key=lambda items: items['commits'], reverse=True)
    
    return lista_ordenada
    
print(commits_por_dia_semana(commits))