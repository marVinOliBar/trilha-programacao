import storage
from interface import(
    registrar_ocorrencia,
)

def main():
    ocorrencias = storage.carregar("ocorrencias.json")
    fire_trucks = storage.carregar("../sistema-viaturas/fire_trucks.json")
    
    print("Sistema de ocorrências integrado")
    
    while True:
        print("\nOpções: ")
        print("1 - Registrar Ocorrência")
        print("0 - Sair do programa")
        
        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Digite apenas números!")
            continue
        
        if opcao == 1:
            registrar_ocorrencia(ocorrencias, fire_trucks)
        elif opcao == 0:
            print("Até logo!")
            break
        else:
            print("Digite uma opção válida!")

if __name__ == "__main__":
    main()