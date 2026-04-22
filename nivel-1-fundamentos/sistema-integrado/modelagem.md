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
