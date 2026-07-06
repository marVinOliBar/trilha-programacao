commits = [
    {"author": "ana", "message": "fix login bug"},
    {"author": "bruno", "message": "add tests"},
    {"author": "ana", "message": "refactor auth"},
    {"author": "carla", "message": "update readme"},
    {"author": "bruno", "message": "fix typo"},
    {"author": "ana", "message": "add logging"},
]

"""Você tem uma lista de commits de um repositório. Cada commit é um dict com author e message. 
Devolva uma lista de dicts com cada autor e quantos commits ele fez, ordenada do maior número de commits pro menor.

Saída esperada
[
    {"author": "ana", "commits": 3},
    {"author": "bruno", "commits": 2},
    {"author": "carla", "commits": 1},
]

FAZ: recebe a lista commits com dicionários de chaves 'author' (str) e 'message' (str) e devolve uma lista de dicionários
com os nomes dos autores e quantidade de commits realizadas. chaves 'author' (str) e 'commits' (int).
ENTRADA: lista commit contendo dicionários com as chaves 'author' (str) e 'message' (str).
SAÍDA: lista contendo dicionários com as chaves 'author' (str) e 'commits' (int)
REGRA:
BLOCO 1
    recebe a lista commits contendo dicionários com as chaves 'author' (str) e 'message' (str) como argumento
    declara uma variavel contador e atribui a ela um dicionario vazio
BLOCO 2 - group by count
    percorre a lista commits
        declara uma variavel chave e atribui a ela o valor da chave 'author' do dicionário
        verifica se não há o valor da variável chave dentro do dicionário contador
            se sim, atribui ao valor da variavel chave dentro do dicionario contador o valor 0
        adiciona ao valor da variavel chave dentro do dicionario contador 1
Bloco 3 - map
    declara a variavel lista_inicial e atribui a ela uma lista vazia
    percorre o dicionario contador
        declara a variavel author e atribui a ela a chave do dicionario
        declara a variavel commit e atribui a ela o valor do dicionario
        adiciona a lista_inicial um dicionario com as chaves 'author' (valor author) e 'commits' (valor commits)
Bloco 4 - sort
declara a variavel lista_ordenada e atribuia a ela a ordenação da lista_inicial de dicionarios 
pelo valor da chave 'commits' do maior para o menor.
retorna com o lista_ordenada
"""
def commits_by_authors(commits):
    
    contador = {}
    for commit in commits:
        chave = commit['author']
        if chave not in contador:
            contador[chave] = 0
        contador[chave] +=1
    
    lista_inicial = [{'author': author, 'commits': qtd_commits} for author, qtd_commits in contador.items()]
        
    lista_ordenada = sorted(lista_inicial, key=lambda item: item['commits'], reverse=True)
    
    return lista_ordenada

print(commits_by_authors(commits))