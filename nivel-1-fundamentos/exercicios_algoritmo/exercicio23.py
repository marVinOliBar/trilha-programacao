"""
O problema:
Você tem a lista de ocorrências atendidas no mês. Cada ocorrência é um dict com o tipo e o período do dia. 
Quer um relatório de quantas ocorrências de cada tipo aconteceram em cada período, da maior quantidade para a menor.
"""
ocorrencias = [
    {"tipo": "incendio", "periodo": "manha"},
    {"tipo": "resgate",  "periodo": "tarde"},
    {"tipo": "incendio", "periodo": "manha"},
    {"tipo": "incendio", "periodo": "noite"},
    {"tipo": "resgate",  "periodo": "manha"},
    {"tipo": "incendio", "periodo": "manha"},
    {"tipo": "resgate",  "periodo": "tarde"},
    {"tipo": "aph",      "periodo": "noite"},
]
"""
Saída esperada (empate na quantidade, ordem tanto faz):
incendio | manha: 3
resgate  | tarde: 2
incendio | noite: 1
resgate  | manha: 1
aph      | noite: 1

FAZ: recebe uma lista de dicts agrupa duas chaves ao mesmo tempo e conta quantas vezes essas chaves agrupadas ocorreram
e retorna um print com as chaves agrupadas e a soma da contagem.
ENTRADA: list de dicts com as keys "tipo" (str) e "periodo" (str)
SAÍDA: uma mensgem formatada as duas keys (str) e a soma da contagem de ocorrências (int). (tipos concretos)
REGRA:
BLOCO 1 - group by count 
    a função recebe a list ocorrencias
    cria uma variavel 'counter' e atribui a ela uma dict vazia
    percorre a lista 'ocorrencias' para cada dict 'ocorrencia'
        cria a variavel 'key' e abribui a ela a tupla com as chaves 'tipo' e 'periodo' de cada ocorrencia
        verifica se a variavel key não está dentro da dict counter
            se sim adiciona atribui 0 a chave 'key' em 'counter'
        soma 1 para cada chave 'key' em 'counter'

BLOCO 2 - map
    criar a variável 'unordered_list' a atribuir a ela uma 'list comprehension' criando uma dict com as keys 'tipo',
    'periodo' e 'soma' atribuindo a elas os valores de 'counter' para cada ('tipo', 'periodo') e 'soma'  

BLOCO 3 - sort
    cria a variavel 'ordered_list' e atribui a ela a função sorted que ordena os itens em 'unordered_list' pelos valores
    em 'soma', do maior para o menor.

BLOCO 3 - retorno
    para cada ocorrencia em ordered_list
        retorna a mensagem formatada: 'tipo' (str) | 'periodo' (str): 'soma' (int)
"""

def ocorrencia_por_periodo(ocorrencias):
    counter = {}
    for ocorrencia in ocorrencias:
        key = (ocorrencia['tipo'], ocorrencia['periodo'])
        if key not in counter:
            counter[key] = 0
        counter[key] += 1
    
    unordered_list = [{'tipo': tipo, 'periodo': periodo, 'soma': soma} for (tipo, periodo), soma in counter.items()]
    
    ordered_list = sorted(unordered_list, key=lambda item: item['soma'], reverse=True)
    
    saida = "\n".join(f"{item['tipo']} | {item['periodo']}: {item['soma']}" for item in ordered_list)
    
    return saida
    

print(ocorrencia_por_periodo(ocorrencias))