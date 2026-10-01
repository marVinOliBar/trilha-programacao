# turma: id_turma, idioma
turmas = [
    (10, "inglês"),
    (20, "espanhol"),
    (30, "francês"),
]

# matricula: aluno, id_turma, situacao
matriculas = [
    ("joão", 20, "ativa"),
    ("maria", 10, "trancada"),
    ("pedro", 30, "ativa"),
    ("ana", 20, "ativa"),
]

# plano: elaborar uma função que recebe como entrada duas listas de tuplas. a saída deverá ser uma lista de tuplas mesclando dados da primeira e da segunda.
# look up: na primeira parte eu faço um dict comprehension e coloco como chave o número da turma e como valor o nome do curso.
# iteração com filtro: na segunda eu crio uma lista vazia, percorro a lista matriculas e vou incluindo na lista criada todas os alunos e cursos que possuem o estado "ativa" em cada matrícula

def matriculas_ativas(turmas, matriculas):
    idioma_por_id_turma = {id_turma:idioma for id_turma, idioma in turmas}
    
    alunos_por_idioma = []
    for aluno, id_turma, situacao in matriculas:
        if situacao == 'ativa':
            alunos_por_idioma.append((aluno, idioma_por_id_turma[id_turma]))
            
    return alunos_por_idioma

print(matriculas_ativas(turmas, matriculas))
    
    