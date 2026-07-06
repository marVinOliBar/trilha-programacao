import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from service import registrar_ocorrencia_service

resultado_1 = registrar_ocorrencia_service(997, "3000-01-05", "teste", "rua 1", "teste")
assert resultado_1[0] == True, f"Caso 1 falhou: {resultado_1}"
assert isinstance(resultado_1[1], int), f"Caso 1: id não é int: {resultado_1}"
print("Caso 1 OK - ocorrência criada com id", resultado_1[1])

resultado_2 = registrar_ocorrencia_service(0, "2026-07-04", "resgate", "rua x", "teste")
assert resultado_2  == (False, "É necessário preencher o número do SDO."), f"Caso 2 falhou: {resultado_2}"
print("Caso 2 OK")

resultado_3 = registrar_ocorrencia_service(997, "3000-01-05", "teste", "rua 1", "teste")
assert resultado_3 == (False, "Esse SDO já existe na data 3000-01-05"), f"Caso 3 falhou: {resultado_3}"
print("Caso 3 OK")