def soma_total(compras):
    
    valores = []
    
    for compra in compras:
        valores.append(compra["preco"])
    
    soma = 0
    
    for valor in valores:
        soma += valor
        
    return soma

def valor_maior(compras):
    
    maior = ("", 0)
        
    for compra in compras:
       if maior[1] < compra["preco"]:
           maior = (compra["item"], compra["preco"])
           
    
    return maior

def valores_na_nota(compras):
    
        
    total = soma_total(compras)
    print(f"A soma total dos valores dos itens é: {total}")
    
    maior = valor_maior(compras)
    print(f"O item com maior valor é o {maior[0]} com o preço de {maior[1]}")