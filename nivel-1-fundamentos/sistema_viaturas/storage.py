import json
def save(fire_trucks):
    with open("fire_trucks.json", "w") as file:
        json.dump(fire_trucks, file, indent=4, ensure_ascii=False)
def load():
    try:
        with open("fire_trucks.json", "r") as file:
            fire_trucks = json.load(file)
            return fire_trucks
    except FileNotFoundError:
        fire_trucks = []
        return fire_trucks

