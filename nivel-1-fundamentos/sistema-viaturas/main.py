import storage
from interface import (
    registry_truck,
    list_truck,
    search_truck,
    remove_truck,
    edit_truck,
)
def main():
    fire_trucks = storage.load()
    while True:
        print("Menu")
        print("")
        print("1 - Registrar")
        print("2 - Listar")
        print("3 - Procurar")
        print("4 - Remover")
        print("5 - Editar")
        print("0 - Sair")
        try:
            option = int(input("Escolha qual sua opção: "))
        except ValueError:
            print("Digitar apenas números")
            continue
        if option == 1:
            registry_truck(fire_trucks)
        if option == 2:
            list_truck(fire_trucks)
        if option == 3:
            search_truck(fire_trucks)
        if option == 4:
            remove_truck(fire_trucks)
        if option == 5:
            edit_truck(fire_trucks)
        if option == 0:
            print("Até logo!")
            break
if __name__ == "__main__":
    main()