from interface import(registrar_viatura,
                      buscar_viatura,
                      remover_viatura,
                      editar_viatura,
                      listar_viatura)

def main():
    
    while True:
        print("MENU")
        print("Digite uma das opções a seguir:")
        print("1 - Registrar Viatura")
        print("2 - Buscar Viatura")
        print("3 - Remover Viatura")
        print("4 - Editar Viatura")
        print("5 - Listar Viatura")
        print("0 - Sair")
        
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("A opção deve ser um número inteiro.")
            continue
        if opcao == 1:
            registrar_viatura()
        elif opcao == 2:
            buscar_viatura()
        elif opcao == 3:
            remover_viatura()
        elif opcao == 4:
            editar_viatura()
        elif opcao == 5:
            listar_viatura()
        elif opcao == 0:
            break
        else:
            print("Número digitado é inválido! Digite novamente.")
            continue

if __name__ == "__main__":
    main()