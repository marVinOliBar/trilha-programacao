funcionarios = [
    {"id": 1, "nome": "Ana", "depto": "TI"},
    {"id": 2, "nome": "Bruno", "depto": "RH"},
    {"id": 3, "nome": "Clara", "depto": "Vendas"},
    {"id": 4, "nome": "Diego", "depto": "Vendas"},
    {"id": 5, "nome": "Elis", "depto": "TI"},
]

vendas = [
    {"id_funcionario": 3, "valor": 1500.00},
    {"id_funcionario": 4, "valor": 2200.00},
    {"id_funcionario": 3, "valor": 800.00},
    {"id_funcionario": 1, "valor": 1200.00},
    {"id_funcionario": 4, "valor": 3100.00},
    {"id_funcionario": 3, "valor": 2500.00},
    {"id_funcionario": 1, "valor": 950.00},
]

"""
Função: total_vendas_por_funcionario
Faz: devolve lista de tuplas (nome, depto, total_vendido), considerando apenas funcionários que tiveram pelo menos uma venda. Ordenada por total decrescente, empate alfabético pelo nome.
Entrada: duas listas de dicionários: funcionarios com chaves 'id' (int), 'nome' (str), 'depto', (str) e vendas, com as chaves 'id_funcionario' (int) e 'valor'. (float)
saída:lista de tuplas (nome, depto, total vendido), considerando apenas funcionários que tiveram pelo menos uma venda. Ordenada por total decrescente, empate alfabético pelo nome.
regra:
. a função recebe duas listas de dicionarios, cruza os dados, pois a lista vendas possui 'id_funcionario' e a lista funcionarios possui 'id' com o mesmo valor, 
calcula o total_vendido pelo funcionário e devovle uma única lista de tuplas (nome, depto, total_vendido)
exceção: não tem, pois não há inserção de dados.
"""

def total_vendas_por_funcionario(funcionarios, vendas):
    funcionarios_por_id = {f["id"]: f for f in funcionarios}
        
    nomes_deptos_total = {}
    for venda in vendas:
        chave = venda["id_funcionario"]
        if chave not in nomes_deptos_total:
            nomes_deptos_total[chave] = 0
        nomes_deptos_total[chave] += venda['valor']
    
    resultado = []
    for id in nomes_deptos_total:
        funcionario = funcionarios_por_id[id]
        nome = funcionario["nome"]
        depto = funcionario["depto"]
        total = nomes_deptos_total[id]
        resultado.append((nome, depto, total))
        
    tupla_ordenada = sorted(resultado, key=lambda r: (-r[2], r[0]))
    
    print(tupla_ordenada)
    
total_vendas_por_funcionario(funcionarios, vendas)