FUNÇÃO: criar_ocorrencia,
FAZ: faz a parte lógica criando as ocorrências da função registrar_ocorrencia,
ENTRADA: ocorrencias, tipo, local, descricao, unit_number,
SAÍDA: o novo dicionário ocorrencia,
REGRA:
.abrir dicionário ocorrencia e inserir as variaveis tipo, local, descrição e unit_number como valores de chaves
.inserir o dicionário na lista ocorrencias
.retornar o dicionário para o registrar_ocorrencia_service
EXCEÇÕES: não há.

FUNÇÃO: registrar_ocorrencia
FAZ: faz a interação com o usuário e o service do programa
ENTRADA: ocorrencias, fire_trucks
SAÍDA: imprime a nova ocorrencia registrada pelo usuário ou erro
REGRA:
.chama função de logica para refinar lista
..se não houver exibir mensagem de erro.
..se houver exibe as viaturas ativas e reserva
.le o prefixo
.le o tipo
.le o local
.le a descricao

"Importar filtrar_viaturas_elegiveis da lógica (junto com o que já tem de import do service).
Função recebe ocorrencias e fire_trucks.
Chama o filtro. Guarda em variável com nome honesto (não result).
Se vazio: print de mensagem, return.
Exibe as viaturas elegíveis (formato sem número sequencial).
Pede input do prefixo. Lembra de .strip() e .upper() (pra normalizar com a regra do service).
Pede input de tipo, local, descrição (com .strip().lower() como na v1).
Chama o service, captura sucesso, dado.
Se sucesso, exibe a ocorrência formatada. Se não, exibe a mensagem de erro."

.chama o service e os coloca em duas variaveis distintas sucesso e dados
.verifica se a variavel sucesso é verdadeira
..se sim exibe para o usuario a nova ocorrencia registrada
..se não exibe mensagem de erro
EXCEÇÕES: não haver viaturas para inserção e service retornar erro

FUNÇÃO: filtrar_viaturas_elegíveis
FAZ: verifica quais viaturas registradas estão em situação ATIVA ou RESERVA e retorna esse resultado para a interface.
ENTRADA: fire_trucks
SAÍDA: lista com as viaturas elegíveis.
REGRA:
.percorre lista com todas as viaturas
..compara a situação das viaturas com ATIVA e RESERVA
...se sim, inserem aquela viatura na nova lista de viaturas elegíveis
...se não, segue o loop
.retorna a nova lista com viaturas elegíveis para a interface
EXCEÇÕES: não há

FUNÇÃO: salvar
FAZ: salva dados no documento informado.
ENTRADA: nome_arquivo, dados
SAÍDA: nenhuma #None. São a mesma coisa
REGRA:
.gravar dados recebidos no arquivo informado
EXCEÇÕES: nenhuma

FUNÇÃO: carregar
FAZ: retorna dados do documento informado para quem chama.
ENTRADA: nome_arquivo
SAÍDA: dados
REGRA:
.tentar abrir o arquivo e ler.
..se o arquivo existir: retorna o que foi lido.
..se o arquivo não existir: retorna lista vazia
EXCEÇÕES: nenhuma

FUNÇÃO: listar_prefixos_viaturas
FAZ: recebe a lista de ocorrencias e devolve lista de viaturas que atenderam ocorrencia
ENTRADA: lista de ocorrencias
SAÍDA: lista de prefixos
REGRA:
. criar variavel lista_viaturas com função set
. percorrer a lista de ocorrencias
. adicionar o prefixo da viatura de cada ocorrencia listada na variavel lista_viaturas
. transformar a variavel lista_viaturas em lista
. retornar o valor da variavel para quem chamou
EXCEÇÕES: não há

FUNÇÃO: ocorrencia_prefixo_selecionado
FAZ: recebe o prefixo escolhido pelo usuario e retorna todas as ocorrencias em que aparece esse prefixo
ENTRADA: lista de ocorrencias e prefixo escolhido pelo usuário
SAÍDA: lista de ocorrencias com o prefixo escolhido.
REGRA:
. cria variavel ocorrencias_filtradas
. percorre a lista de ocorrencias
. compara se o prefixo selecionado é igual ao prefixo da lista de ocorrencias (a comparação tratará com upper() para os dois lados)
.. se igual, adiciona aquela ocorrencia na variavel ocorrencias_filtradas
. retorna o valor da variavel
EXCEÇÕES: não há

FUNÇÃO: consultar_ocorrencia_viaturas_service
FAZ: valida opção do usuario, chama a logica e retorna valores para o usuario.
ENTRADA: ocorrencias e opcao_prefixo
SAÍDA: mensagem de erro ou dados
REGRA:
. chama a função listar_prefixos_viaturas e coloca na variavel elegiveis
. verifica se a opcao_prefixo não está em elegiveis
.. se não retorna tupla (Falso, mensagem de erro)
. chama a função ocorrencia_prefixo_selecionado e coloca o resultado na variavel ocorrencias_filtradas
. retorna tupla (Verdadeiro, ocorrencias_filtradas para interface)
EXCEÇÕES: nenhuma.

FUNÇÃO: consultar_ocorrencia_viaturas
FAZ: exibe as ocorrencias da viatura consultada.
ENTRADA: lista ocorrencias
SAÍDA: exibe dados ao usuário ou mensagem de erro.
REGRA:
. chamar a função listar_prefixos_viaturas e atribuir à variavel lista_prefixos que será criada.
. se não tiver nada em lista_prefixos, exibir mensagem que não há ocorrencias registradas e retornar
. abrir loop para lista_prefixos e exibir os itens da lista.
. ler a opção do usuário, normalizando com strip() e upper()
. chamar a função consultar_ocorrencias_viaturas_service e passar a lista ocorrencias e opção do usuário como argumento e atribuir retorno a variaveis sucesso e dados
. se sucesso for verdadeiro, exibir dados para o usuario
. se sucesso for falso, exibir mensagem de erro para o usuario
EXCEÇÕES: não há.

FUNÇÃO: registrar_ocorrencia_storage
FAZ: salva a ocorrencia recem registrada no banco de dados
ENTRADA: dicionário contendo sdo, data, tipo, local e descrição da ocorrencia
SAÍDA: tupla contendo sdo, data, tipo, local e descrição da ocorrencia
REGRA:
.função recebe o dicionário com os valores das ocorrencias e devolve uma tupla com os valores da ocorrencia
para ser salva no banco de dados
EXCEÇÕES: nenhuma
