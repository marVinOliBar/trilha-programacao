from exercicio33 import verifica_concomitancia

def test_atendimento_comeca_no_meio_do_outro():
    assert verifica_concomitancia(("09:00", "10:00"),("09:30", "10:30")) is True

def test_atendimento_fica_inteiro_dentro_do_outro():
    assert verifica_concomitancia(("09:00", "10:00"),("09:05", "09:55")) is True
    
def test_um_termina_na_hora_exata_em_que_o_outro_começa():
    assert verifica_concomitancia(("09:00", "10:00"),("10:00", "11:00")) is False
    
def test_segundo_atendimento_vem_inteiro_antes_do_primeiro():
    assert verifica_concomitancia(("11:00", "12:00"),("09:00", "10:00")) is False
    
def test_segundo_atendimento_vem_inteiro_depois_do_primeiro():
    assert verifica_concomitancia(("09:00", "10:00"),("11:00", "12:00")) is False