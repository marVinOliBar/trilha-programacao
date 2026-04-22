from service import (
    registry_truck_service,
    list_truck_service,
    search_truck_service,
    remove_truck_service,
    edit_truck_service,
)

def registry_truck(fire_trucks):
    unit_number = input("Digite o prefixo da viatura: ").lower()
    mileage = input("Digite a quilometragem de viatura: ").lower()
    station = input("Digite a Estação onde a viatura permanecerá: ").lower()
    status = input("Digite a situação da viatura: ATIVA | RESERVA | BAIXA: ").lower()
    
    sucess, data = registry_truck_service(fire_trucks, unit_number, mileage, station, status)
    
    if sucess:
        print(f"A viatura {data['prefixo']}, foi registrada com sucesso!")
    else:
        print(data)

def list_truck(fire_trucks):

    sucess, data = list_truck_service(fire_trucks)

    if sucess:
        for i, d in enumerate(data, start=1):
            print(f"ID: {i} - Unidade de Serviço: {d['prefixo']} - Quilometragem: {d['quilometragem']} - Estação a que pertence: {d['estacao']} - Situação: {d['situacao']}")
    else:
        print(data)

def search_truck(fire_trucks):
        
    truck = input("Digite o termo que deseja encontrar: ").lower()
    
    sucess, data = search_truck_service(fire_trucks, truck)
    
    if sucess:
        for i in data:
            print(f"Unidade de Serviço: {i['prefixo']} - Quilometragem: {i['quilometragem']} - Estação a que pertence: {i['estacao']} - Situação: {i['situacao']}")
    else:
        print(data)

def remove_truck(fire_trucks):
    
    list_truck(fire_trucks)
    
    try:
        option = int(input("Escolha o ID da viatura que deseja remover: "))
    except ValueError:
        print("Digite apenas números!")
        return
    
    sucess, data = remove_truck_service(fire_trucks, option)
    
    if sucess:
        print(f"A viatura {data['prefixo']} foi removida.")
        return
    else:
        print(data)

def edit_truck(fire_trucks):
    
    list_truck(fire_trucks)
    
    try:
        option = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite apenas números!")
        return
    
    new_truck_number = input("Digite o novo prefixo: ").lower()
    new_mileage = input("Digite a nova quilometragem: ").lower()
    new_station = input("Digite a nova Estação: ").lower()
    new_status = input("Digite o novo Status: ").lower()
    
    sucess, data = edit_truck_service(fire_trucks, option, new_truck_number,
                       new_mileage, new_station, new_status)
    
    if sucess:
        print(f"A viatura {data['prefixo']} foi editada com sucesso!")
    else:
        print(data)