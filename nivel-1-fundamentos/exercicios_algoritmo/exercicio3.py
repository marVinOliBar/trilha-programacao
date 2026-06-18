alunos = [
    {"nome": "Ana", "notas": [7.0, 8.5, 6.0]},
    {"nome": "Bruno", "notas": [5.0, 4.5, 6.0]},
    {"nome": "Clara", "notas": [9.0, 9.5, 10.0]},
    {"nome": "Diego", "notas": [3.0, 5.0, 4.0]},
]

# Calcular a média de cada aluno e dizer quem foi aprovado (média >= 7.0) e quem foi reprovado.

"""
. pegar cada dicionário de alunos
. calcular a média dos alunos
. verificar se é >= 7 e fazer o print respectivo (aprovado ou reprovado)
. devolver isso em lista?
. imprimir tudo na tela?
"""
def avaliar_alunos(alunos):
    avaliados = []
    for aluno in alunos:
        soma = 0
        media = 0
        for nota in aluno["notas"]:
            soma += nota
        media = soma / 3
        if media >= 7:
            avaliados.append((aluno["nome"], media, "Aprovado"))
        else:
            avaliados.append((aluno["nome"], media, "Reprovado"))
    
    for avaliado in avaliados:
        print(f"O {avaliado[0]} tem a media {avaliado[1]:.1f} e está {avaliado[2]}")