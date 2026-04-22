import storage
from logic import (
    create_truck,
    find_truck,
    delete_truck,
    modify_truck,
)

def registry_truck_service(fire_trucks, unit_number, mileage, station, status):
    if not unit_number:
        return (False, "É obrigatório registrar um prefixo!")
    if not mileage:
        return (False, "É obrigatório registrar uma quilometragem!")
    if not station:
        return (False, "É obrigatório registrar uma estação!")
    if not status:
        return (False, "É obrigatório registrar uma situação!")
    fire_truck = create_truck(fire_trucks, unit_number, mileage, station, status)
    storage.save(fire_trucks)
    return (True, fire_truck)

def list_truck_service(fire_trucks):
	if not fire_trucks:
		return (False, "Não há viaturas registradas!")
	else:
		return (True, fire_trucks)

def search_truck_service(fire_trucks, truck):
    
    sucess, result = list_truck_service(fire_trucks)
    
    if not sucess:
        return (False, "Nâo foram registradas viaturas!")
    else:
        a, resp = find_truck(fire_trucks, truck)
        if not a:
            return (False, "Não foram encontradas viaturas!")
        else:
            return (True, resp)

def remove_truck_service(fire_trucks, option):

    if not fire_trucks:
        return (False, "Não há viaturas cadastradas!")
    else:
        if option < 1 or option > len(fire_trucks):
            return (False, "Escolha uma opção válida!")
        else:
            result = delete_truck(fire_trucks, option)
            storage.save(fire_trucks)
            return (True, result)

def edit_truck_service(fire_trucks, option, new_truck_number,
                       new_mileage, new_station, new_status):
    
    if not fire_trucks:
        return (False, "Não há viaturas registradas!")
    else:
        if option < 1 or option > len(fire_trucks):
            return (False, "Escolha uma opção válida!")
        else:
            result = modify_truck(fire_trucks, option, new_truck_number,
                new_mileage, new_station, new_status)
            
            storage.save(fire_trucks)
            return (True, result)
