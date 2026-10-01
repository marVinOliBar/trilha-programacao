from datetime import datetime

def normalizar_inicio(texto):
    inicio = datetime.strptime(texto, "%Y-%m-%d %H:%M")
    return inicio.strftime("%Y-%m-%d %H:%M")
    
horarios = ["2026-10-1 8:00", "2026-10-01 08:00", "2026-10-01 8:00", "2026-10-1 08:00", "2026-10-1 9:30",]
print([normalizar_inicio(horario) for horario in horarios])