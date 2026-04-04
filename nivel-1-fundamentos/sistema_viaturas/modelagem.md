FUNÇÃO: edit_truck_service(fire_trucks, option, new_truck_number, new_mileage, new_station, new_status)
ENTRADA: lista fire_trucks e opção do usuario, novo prefixo, nova quilometragem, nova estação e nova situação.
SAÍDA: resposta true com dicionário devolvido pela lógica ou false com explicação do erro.
FLUXO:
. testa se a opção do usuario é valida
.. se invalida retorna false e mensagem de erro
.. se valida:
... chama a função modify_truck() e atribui a uma variável
... salva a lista modificada na persistência
... retorna true e a variavel com o novo dicionário
EXCEÇÃO: opção inválida

FUNÇÃO: modify_truck(fire_trucks, option, new_truck_number, new_mileage, new_station, new_status)
ENTRADA: lista fire_trucks e opção do usuario, novo prefixo, nova quilometragem, nova estação e nova situação.
SAÍDA: dicionário modificado.
FLUXO:
. recebe os dados de edit_truck_service
. converte opção do usuário em indice da lista
. atribui novos valores as chaves do dicionário apontado pelo indice.
. atribui o dicionário modificado a nova variável
. retorna a nova variável com o dicionário modificado.
EXCEÇÃO: não tem
