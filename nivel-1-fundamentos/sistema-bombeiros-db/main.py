from interface import(registrar_viatura)

def main():
    
    while True:
        print("MENU")
        print("Digite uma das opções a seguir:")
        print("1 - Registrar Viatura")
        print("0 - Sair")
        
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            print("A opção deve ser um número inteiro.")
            continue
        
        if opcao == 1:
            registrar_viatura()
            
        elif opcao == 0:
            break
        
        else:
            print("Número digitado é inválido! Digite novamente.")
            continue
        
if __name__ == "__main__":
    main()