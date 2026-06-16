from storage import(carregar)
from interface import(registrar_livros)

def main():
    livros = carregar()
    
    print("GERENCIADOR DE BIBLIOTECA")
    while True:
        print("Opções: ")
        print("1 - Registrar livro")
        print("0 - Sair")
        
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            registrar_livros(livros)
        
        if opcao == 0:
            break
        
if __name__ == "__main__":
    main()