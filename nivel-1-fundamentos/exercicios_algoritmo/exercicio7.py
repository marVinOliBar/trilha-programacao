funcionarios = [
    {"nome": "Ana", "cargo": "analista", "salario": 4500.00},
    {"nome": "Bruno", "cargo": "gerente", "salario": 9800.00},
    {"nome": "Clara", "cargo": "analista", "salario": 4200.00},
    {"nome": "Diego", "cargo": "estagiário", "salario": 1800.00},
    {"nome": "Elis", "cargo": "gerente", "salario": 10500.00},
    {"nome": "Fábio", "cargo": "analista", "salario": 5100.00},
]

"""
Mostrar a lista de cargos únicos que existem na empresa, em ordem alfabética.
Mostrar os funcionários ordenados pelo salário, do maior pro menor.
"""

def cargos_unicos(funcionarios):
    cargos = []
    for funcionario in funcionarios:
        cargos.append(funcionario["cargo"])
    unicos = set(cargos)
    print(sorted(unicos))

cargos_unicos(funcionarios)



def funcionarios_ordenados_salario(funcionarios):
    funcionarios_ordenados = sorted(funcionarios, key=lambda funcionario: funcionario["salario"], reverse=True)    
    for funcionario in funcionarios_ordenados:
        print(funcionario)

funcionarios_ordenados_salario(funcionarios)