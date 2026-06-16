"""
Registrar livors com título e autor
"""
from service import(registrar_livro_service)

def registrar_livros(livros):
    titulo = input("Digite o título do livro: ").lower().strip()
    autor = input("Digite o autor do livro: ").lower().strip()
    
    sucesso, dado = registrar_livro_service(livros, titulo, autor)
    
    
    if sucesso:
        print(f"O livro {dado['titulo']} do autor {dado['autor']} foi registrado na biblioteca")
    else:
        print(dado)