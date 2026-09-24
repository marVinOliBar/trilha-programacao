barbeiros = [
    (1, "carlos"),
    (2, "rafa"),
]

agendamentos = [
    (2, "2026-09-25 09:00"),
    (1, "2026-09-25 09:30"),
    (2, "2026-09-25 10:00"),
]

def horarios_por_barbeiro(barbeiros, agendamentos):
    # é necessário fazer look up da lista barbeiros
    barbeiro_por_id = {id_barbeiro: barbeiro for id_barbeiro, barbeiro in barbeiros} 
    
    horarios_agendados = []
    for id_barbeiro, horario in agendamentos:
        barbeiro = barbeiro_por_id[id_barbeiro]
        horarios_agendados.append((horario, barbeiro))
    
    return horarios_agendados

print(horarios_por_barbeiro(barbeiros, agendamentos))