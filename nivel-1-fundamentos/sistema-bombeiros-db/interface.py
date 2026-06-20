from service import(registrar_viatura_service)

def registrar_viatura():
    
    prefixo = input("Digite o prefixo da viatura:").lower().strip()
    
    try:
        quilometragem = int(input("Digite a quilometragem da viatura: "))
    except ValueError:
        print("Quilometragem precisa ser um número inteiro.")
        return 
    
    estacao = input("Digite a Estação em que a viatura opera: ").lower().strip()
    situacao = input("Digite a situação da viatura: operando | manutencao | baixada: ").lower().strip()
    
    sucesso, dado = registrar_viatura_service(prefixo, quilometragem, estacao, situacao)
    
    if sucesso:
        print(f"A viatura {dado} foi registrada com sucesso.")
        return
    else:
        print(dado)
        return