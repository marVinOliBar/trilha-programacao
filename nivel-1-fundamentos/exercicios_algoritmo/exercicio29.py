donos = [
    (1, "Ana"),
    (2, "Bruno"),
]

animais = [
    ("Rex", 1),
    ("Mimi", 2),
    ("Toby", 1),
]

def animais_e_donos(donos, animais):
    nomes = {identidade: nome for identidade, nome in donos}
    
    bichos_donos = []
    for bichos, identidade in animais:
        dono = nomes[identidade]
        bichos_donos.append((bichos, dono))
    
    return bichos_donos

print(animais_e_donos(donos, animais))