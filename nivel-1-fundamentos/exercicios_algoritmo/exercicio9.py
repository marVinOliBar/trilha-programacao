funcionarios = [
    {"nome": "Ana", "depto": "TI", "salario": 5500, "ativo": True},
    {"nome": "Bruno", "depto": "RH", "salario": 4200, "ativo": False},
    {"nome": "Clara", "depto": "TI", "salario": 6800, "ativo": True},
    {"nome": "Diego", "depto": "Vendas", "salario": 3900, "ativo": True},
    {"nome": "Elis", "depto": "TI", "salario": 5500, "ativo": True},
    {"nome": "Fábio", "depto": "RH", "salario": 4200, "ativo": True},
    {"nome": "Gisele", "depto": "Vendas", "salario": 7200, "ativo": False},
]
"""
devolve só os funcionários ativos, ordenados por:

Departamento (alfabético)
Dentro do depto, salário (decrescente — maior primeiro)
Empate de salário, nome (alfabético)
"""

def lista_funcionarios_ativos(funcionarios):
    funcionarios_ativos = []
    for funcionario in funcionarios:
        if funcionario["ativo"]:
            funcionarios_ativos.append(funcionario)
            
    ordenado = sorted(funcionarios_ativos, key=lambda f: (f['depto'], -f['salario'], f['nome']))
    for o in ordenado:
        print(o)
    
lista_funcionarios_ativos(funcionarios)
