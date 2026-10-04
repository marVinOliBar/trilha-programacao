from datetime import datetime

def verifica_concomitancia(reserva_a, reserva_b):
    inicio_a, termino_a = reserva_a
    inicio_b, termino_b = reserva_b
    return inicio_a < termino_b and inicio_b < termino_a
    



pares = [
    (("09:00", "09:30"), ("09:15", "09:45")),
    (("09:00", "09:30"), ("09:30", "10:00")),
    (("14:00", "15:00"), ("14:20", "14:40")),
    (("15:00", "15:30"), ("14:00", "14:30")),
    (("10:00", "10:30"), ("09:45", "10:15")),
]

print([verifica_concomitancia(a, b) for a, b in pares])