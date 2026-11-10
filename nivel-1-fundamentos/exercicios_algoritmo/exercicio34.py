agenda_1 = [
    ("carlos", "15:00", "15:30"),
    ("ana", "09:00", "09:30"),
    ("bia", "10:00", "10:45"),
    ("davi", "09:30", "10:00"),
]

agenda_2 = [
    ("davi", "10:30", "11:00"),
    ("carlos", "15:00", "15:30"),
    ("ana", "09:00", "09:30"),
    ("bia", "10:00", "10:45"),
]
"""
primeira função
1. preciso desempacotar as tuplas em variáveis próprias descartando o nome
2. retorno a comparação da inicio e fim das reservas

segunda função
1. aqui a ordenção precisa apontar para ordenação do índice 1 da tupla (início) e depois pegar o resultado ordenado e colocar em uma variável.
2. depois eu percorro a nova variavel em seu limite de de índices
3. nomeio duas variaveis e atribuo a elas o indice atual e indice +1 respectivamente
4. verifico se é verdadeiro o resultado da primeira função passando como parametros as variaveis que receberam indice atual e indice +1
5. retorno True se há conflito
6. saio do loop e retorno False se todas as comparações não acusaram True
"""

def conflitam(agenda_1, agenda_2):
    _, inicio_a, fim_a = agenda_1
    _, inicio_b, fim_b = agenda_2
    return inicio_a < fim_b and inicio_b < fim_a

def sala_tem_conflito(agendas):
    ordenadas = sorted(agendas, key=lambda agenda: agenda[1], reverse=True)
    for i in range(len(ordenadas) - 1):
        atual = ordenadas[i]
        seguinte = ordenadas[i + 1]
        print(atual, seguinte)
        if conflitam(atual, seguinte):
            return True
    return False
    
print(sala_tem_conflito(agenda_1), sala_tem_conflito(agenda_2))
