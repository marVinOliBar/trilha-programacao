from exercicio34 import sala_tem_conflito

def test_atendimentos_que_encostam():
    assert sala_tem_conflito([("carlos", "15:00", "15:30"), ("ana", "15:30", "16:00")]) is False
    
def test_atendimentos_não_vizinhos():
    assert sala_tem_conflito(
        [("ana", "09:00", "09:30"),("carlos", "15:00", "15:30"), ("bia", "09:25", "10:00")]) is True
    
def test_no_ultimo_par():
    assert sala_tem_conflito(
        [("carlos", "10:29", "11:00"),
        ("ana", "09:00", "09:30"),
        ("bia", "10:00", "10:30"),
        ("davi", "09:30", "10:00")]) is True
    
def test_agenda_vazia():
    assert sala_tem_conflito([]) is False
    
def test_agenda_com_um_atendimento():
    assert sala_tem_conflito([("carlos", "15:00", "15:30")]) is False