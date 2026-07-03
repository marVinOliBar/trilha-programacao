funcionarios = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Bruno"},
    {"id": 3, "nome": "Carla"},
    {"id": 4, "nome": "Diego"},
]

salarios = [
    {"funcionario_id": 1, "salario": 5000.0},
    {"funcionario_id": 2, "salario": 7500.0},
    {"funcionario_id": 4, "salario": 6200.0},
]
"""
FAZ: recebe duas listas com dicionários (funcionários e salários) de entrada e retorna uma única lista filtrada
nomes_e_salarios ordenada do salário maior para o menor.
ENTRADA: lista funcionario com dicionarios de chaves 'id' (int) e 'nome' (str), e lista salarios com dicionarios de 
chaves 'funcionario_id' (int) e 'salario' (float)
SAÍDA: uma lista nomes_e_salarios de dicionarios de chaves 'nome' (str) e 'salario' (float)
REGRA: a função recebe duas listas de dicionarios (funcionario e salario), relaciona as duas por meio das
chaves ('id', 'funcionario_id') respectivamente e devolve uma lista de dicionarios nomes_e_salarios 
com as chaves 'nome' e 'salario', apenas com funcinarios que tem salario cadastrado e ordenada por salario do maior para
o menor. 
EXCEÇÃO: "não há exceção a tratar — o enunciado garante que as listas vêm bem formadas e 
funcionários sem salário simplesmente não entram no resultado (filtro implícito, não é erro)."
"""
def join_filtro_ordenacao(funcionarios, salarios):
    funcionarios_por_id = {f["id"]:f for f in funcionarios}
    salarios_por_id = {s["funcionario_id"]:s["salario"] for s in salarios}
    
    resultado = []
    for id in salarios_por_id:
        funcionario = funcionarios_por_id[id]
        nome = funcionario['nome']
        salario = salarios_por_id[id]
        resultado.append({'nome': nome, 'salario': salario})

    
    nomes_e_salarios = sorted(resultado, key=lambda r: r["salario"], reverse=True)
        
    return nomes_e_salarios

print(join_filtro_ordenacao(funcionarios, salarios))