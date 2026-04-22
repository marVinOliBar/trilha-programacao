def create_truck(fire_trucks, unit_number, mileage, station, status):
    fire_truck = {
        'prefixo': unit_number,
        'quilometragem': mileage,
        'estacao': station,
        'situacao': status,
    }
    fire_trucks.append(fire_truck)
    return fire_truck

def find_truck(fire_trucks, truck):
    
    result = []
    for i, tr in enumerate(fire_trucks, start=1):
        for valor in tr.values():
            if truck in str(valor).lower():
                result.append(tr)
            
    if result:
        return (True, result)
    else:
        return (False, result)

def delete_truck(fire_trucks, option):
    
    index = option - 1
    return fire_trucks.pop(index)
    
def modify_truck(fire_trucks, option, new_truck_number,
                       new_mileage, new_station, new_status):
    index = option - 1
    new_truck = {}
    
    for i, truck in enumerate(fire_trucks):
        if index == i:
            truck['prefixo'] = new_truck_number
            truck['quilometragem'] = new_mileage
            truck['estacao'] = new_station
            truck['situacao'] = new_status
            new_truck = truck
    
    return new_truck