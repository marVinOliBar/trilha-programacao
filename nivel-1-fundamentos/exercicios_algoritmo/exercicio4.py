"""
ENUNCIADO
Receber um número mínimo de estoque (por exemplo, 10).
Listar os produtos que estão abaixo desse mínimo, mostrando o nome,
a quantidade atual e quanto custaria repor até chegar no mínimo.
Exemplo: se o mínimo é 10, o caderno tem 3 unidades — faltam 7.
Custo de reposição: 7 × 15.90 = 111.30.
"""
estoque = [
    {"produto": "caneta", "quantidade": 150, "preco": 2.50},
    {"produto": "caderno", "quantidade": 3, "preco": 15.90},
    {"produto": "borracha", "quantidade": 80, "preco": 1.75},
    {"produto": "mochila", "quantidade": 2, "preco": 89.90},
    {"produto": "lápis", "quantidade": 45, "preco": 1.20},
    {"produto": "estojo", "quantidade": 5, "preco": 32.00},
]

"""
MODELAGEM
ENTRA: lista estoque que contém dicionários.
SAI: lista de produtos abaixo do mínimo (nome, quantidade atual e 
quanto custa repor até o mínimo)
REGRA:
. estipular valor minimo de estoque (seguindo exemplo: 10),
. declarar variavel reposicao e atribuir lista vazia,
. declarar variavel custo e atribuir 0,
. ler cada uma das quantidades de cada dicionário,
.. se estiver abaixo do mínimo,
.. verificar quantas unidades faltam para chegar no minimo,
.. multiplicar qtde que falta pelo valor da chave "preco" e 
guardar isso na variavel custo.
. acrescentar na variavel reposicao tupla com valores da chaves
"produto", "quantidade" e "custo"
. listar na tela a impressão das tuplas. uma por linha. 
EXCEÇÃO: pegar produtos que não precisam de reposição, fazer cálculo
errado de custo para reposição, imprimir resultado errado.
"""

def custo_reposicao(estoque):
    
    minimo = 10
    
    reposicao = []
    
    for item in estoque:
        custo = 0
        if item["quantidade"] < minimo:
            falta = minimo - item["quantidade"]
            custo = falta * item["preco"]
            reposicao.append((item["produto"], item["quantidade"], custo))
    
    if reposicao:    
        print("É necessário repor os seguintes itens:")
        for produto, quantidade, custo in reposicao:
            print(f"Produto: {produto} | Qtde: {quantidade} | Custo: R${custo}.")
    else:
        print("Não existem produtos abaixo do mínimo")

custo_reposicao(estoque)