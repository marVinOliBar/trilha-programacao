funcionarios = [
    {"nome": "Ana", "cargo": "analista", "salario": 4500, "ativo": True},
    {"nome": "Bruno", "cargo": "gerente", "salario": 9800, "ativo": False},
    {"nome": "Clara", "cargo": "analista", "salario": 5200, "ativo": True},
    {"nome": "Diego", "cargo": "estagiário", "salario": 1800, "ativo": True},
    {"nome": "Elis", "cargo": "gerente", "salario": 10500, "ativo": True},
    {"nome": "Fábio", "cargo": "analista", "salario": 4800, "ativo": True},e
    {"nome": "Gisele", "cargo": "estagiário", "salario": 2000, "ativo": False},
]

#Lista com os nomes de todos os funcionários ativos.
funcionarios_ativos = [funcionario["nome"] for funcionario in funcionarios if funcionario["ativo"]]
print(funcionarios_ativos)
#Lista com os nomes dos funcionários que ganham mais de 4000 (independente de ativos ou não).
funcionarios_ricos = [funcionario["nome"] for funcionario in funcionarios if funcionario["salario"] > 4000]
print(funcionarios_ricos)
#Lista de tuplas (nome, salario_com_aumento_10%) apenas dos analistas ativos.
nome_e_salario_aumentado = [(funcionario["nome"], funcionario["salario"] * 1.10) for funcionario in funcionarios
                            if funcionario["cargo"] == "analista" and funcionario["ativo"]]
print(nome_e_salario_aumentado)
#[expressao for item in lista if condicao]


