from logica import(
    filtrar_viaturas_elegiveis
)

from service import(
    registrar_ocorrencia_service
)

def registrar_ocorrencia(ocorrencias, fire_trucks):
    
    elegiveis = filtrar_viaturas_elegiveis(fire_trucks)
    
    if not elegiveis:
        print("Não há viaturas para serem inseridas na ocorrência!")
        return
    
    for elegivel in elegiveis:
        print(f"{elegivel['prefixo']} ({elegivel['situacao']})")
    
    unit_number = input("Digite o prefixo da viatura que atende esta ocorrência: ").strip().upper()
    tipo = input("Digite o tipo da ocorrência: ").strip().lower()
    local = input("Digite o local da ocorrência: ").strip().lower()
    descricao = input("Digite a descrição da ocorrência: ").strip().lower()
    
    sucesso, dados = registrar_ocorrencia_service(ocorrencias, fire_trucks, tipo, local, descricao, unit_number)
    
    if sucesso:
        print(f"Ocorrência {dados['tipo']} do {dados['prefixo']} registrada com sucesso")
    else:
        print(dados)