from service import(registrar_viatura_service,
                    buscar_viatura_service,
                    remover_viatura_service,
                    editar_viatura_service,
                    listar_viatura_service,
                    registrar_ocorrencia_service,)

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
    
def buscar_viatura():
    termo = input("Digite o termo de busca (prefixo): ")
    
    sucesso, dado = buscar_viatura_service(termo)
    
    if sucesso:
        for linha in dado:
            prefixo, quilometragem, estacao, situacao = linha
            print(f"Prefixo: {prefixo} | Quilometragem: {quilometragem} | Estação: {estacao} | Situação: {situacao}")
    else:
        print(dado)
        
def remover_viatura():
    prefixo = input("Digite o prefixo da viatura que deseja remover: ").lower().strip()
    sucesso, dado = remover_viatura_service(prefixo)
    if not sucesso:
        print(dado)
    else:
        print(f"Você removeu a viatura {prefixo} com sucesso.")
        
def editar_viatura():
    prefixo = input("Digite o prefixo da viatura que deseja editar: ").lower().strip()
    try:
        quilometragem = int(input("Digite a nova quilometragem da viatura: "))
    except ValueError:
        print("Digite um valor válido!")
        return
    estacao = input("Digite a nova estação da viatura: ").lower().strip()
    situacao = input("Digite a situacao da viatura: operando | manutencao | baixada: ").lower().strip()
    
    sucesso, dado = editar_viatura_service(prefixo, quilometragem, estacao, situacao)
    
    if not sucesso:
        print(dado)
    else:
        print(f"A viatura {prefixo} foi editada com sucesso!")
        
def listar_viatura():
    sucesso, dado = listar_viatura_service()
    
    if sucesso:
        for linha in dado:
            prefixo, quilometragem, estacao, situacao = linha
            print(f"Prefixo: {prefixo} | Quilometragem: {quilometragem} | Estação: {estacao} | Situação: {situacao}")
    else:
        print(dado)
        
def registrar_ocorrencia():
    try:
        sdo = int(input("Entre com o número do SDO: "))
    except ValueError:
        print("É necessário entrar com um número inteiro")
        return
        
    data = input("Digite a data da ocorrência: ").strip()
    tipo = input("Digite o tipo da ocorrência: ").lower().strip()
    local = input("Digite o local da ocorrência: ").lower().strip()
    descricao = input("Digite a descrição da ocorrência: ").lower().strip()
    
    sucesso, dado = registrar_ocorrencia_service(sdo, data, tipo, local, descricao)
    
    if not sucesso:
        print(dado)
    else:
        print(f"A ocorrência de SDO nº {sdo} da data {data} foi gerada com sucesso.")