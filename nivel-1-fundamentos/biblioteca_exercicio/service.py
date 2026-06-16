"""
Validação no service: 
não aceita título vazio, 
não aceita autor vazio,
não aceita livro duplicado (mesmo título + mesmo autor).
"""
from storage import(salvar)
from logica import(criar_livro)

def registrar_livro_service(livros, titulo, autor):
    
    if not titulo:
        return (False, "nenhum título foi inserido.")
    if not autor:
        return (False, "nenhum autor foi inserido.")
    
    for livro in livros:
        if titulo == livro["titulo"] and autor == livro["autor"]:
            return (False, "esse livro já está cadastrado.")
    
    novo_livro = criar_livro(titulo, autor)
    
    livros.append(novo_livro)
    
    salvar(livros)
    
    return (True, novo_livro)