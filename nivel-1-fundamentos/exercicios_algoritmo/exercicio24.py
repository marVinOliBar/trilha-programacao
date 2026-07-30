bugs = [
    {"id": 1, "severidade": "alta",   "componente": "auth"},
    {"id": 2, "severidade": "baixa",  "componente": "ui"},
    {"id": 3, "severidade": "alta",   "componente": "auth"},
    {"id": 4, "severidade": "media",  "componente": "auth"},
    {"id": 5, "severidade": "alta",   "componente": "database"},
    {"id": 6, "severidade": "baixa",  "componente": "ui"},
    {"id": 7, "severidade": "alta",   "componente": "auth"},
    {"id": 8, "severidade": "media",  "componente": "database"},
    {"id": 9, "severidade": "baixa",  "componente": "ui"},
    {"id": 10, "severidade": "alta",  "componente": "database"},
]

"""
Saída esperada:

[
    {"severidade": "alta",  "componente": "auth",     "quantidade": 3},
    {"severidade": "baixa", "componente": "ui",       "quantidade": 3},
    {"severidade": "alta",  "componente": "database", "quantidade": 2},
    {"severidade": "media", "componente": "auth",     "quantidade": 1},
    {"severidade": "media", "componente": "database", "quantidade": 1},
]

FAZ: recebe a lista bugs com dicts de chaves 'id', 'severidade' e 'quantidade' agrupa os bugs por 'severidade' e 'componente' e retorna a quantidade de vezes que ocorreu.
ENTRADA: lista bugs com dicts de chaves 'id' (int), 'severidade' (str), 'componente' (str).
SAÍDA: lista de dicts com chaves 'severidade' (str), 'componente' (str) e 'quantidade' (int).
 REGRA:
    recebe a lista bugs com dicts

BLOCO - group by count
    cria uma variável contador e atribui um dicionário vazio
    percorre a lista bugs para cada bug
        cria a variavel chave e atribui a tupla de chaves 'severidade' e 'componente' em bug
        verifica se chave não está em contador
            se sim, atribui à chave em contador o valor 0
        incrementa à chave em contador o valor 1
        
BLOCO 2 - MAP
    cria a variavel lista_agrupada e atribui a ela uma lista com dicts de chaves 'severidade', 'componente' e 'quantidade' percorrendo os itens de contador, desempacotando para
uma tupla com severidade e componente e uma variável quantidade.

BLOCO 3 - SORT
    cria a variavel lista_ordenada e atribui a ela a função sorted que ordena a variavel lista_agrupada pela chave 'quantidade' do maior para o menor e em caso de empate, faz ordem
alfabética pela chave 'severidade'.

    retorna a lista_ordenada.
"""

def contador_bugs(bugs):
    contador = {}
    for bug in bugs:
        chave = (bug['severidade'], bug['componente'])
        if chave not in contador:
            contador[chave] = 0
        contador[chave] += 1
    
    lista_agregada = [{'severidade': severidade, 'componente': componente, 'quantidade': quantidade} for (severidade, componente), quantidade in contador.items()]

    lista_ordenada = sorted(lista_agregada, key=lambda item: (-item['quantidade'], item['severidade']))

    return lista_ordenada
    
print(contador_bugs(bugs))