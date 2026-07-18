FAZ: imprime no terminal os prefixos das viaturas em situação "operando", um por linha.
ENTRADA: nenhuma (lê do bombeiros.db).
SAÍDA: prefixos no terminal, um por linha.
REGRA:

1. Conectar ao banco.
2. SELECT prefixo WHERE situacao = 'operando'.
3. Iterar e imprimir cada prefixo.
4. Fechar conexão.
   EXCEÇÕES: tabela vazia (imprime nada) ou nenhuma viatura operando (imprime nada).

FAZ: testa as constraints implementadas.
ENTRADA: nenhuma (lê do bombeiros.db).
SAÍDA: 4 mensagens de erro.
REGRA:
. Conectar ao banco.
. Testar PK fazendo inserção de viatura já existente.
. Testar NOT NULL fazendo inserção de viatura sem estacao declarada.
. Testar CHECK fazendo inserção de viatura com situacao 'em deslocamento'.
. Testar PK fazendo inserção de viatura sem prefixo declarado.
. Para cada tentativa, capturar o erro e mostrar mensagem.
EXCEÇÕES: algum dos constraints não pegar o erro.

TABELA: atendimento
FAZ: a junção da tabela viatura (atributo prefixo) com a tabela ocorrência (atributo id).
ATRIBUTOS (nome + tipo + constraints):
. prefixo + TEXT + NOT NULL
. id + INTEGER + NOT NULL
RELAÇÕES (com quem se liga e como): atributo prefixo se liga a tabela viatura e id se liga a tabela ocorrencia.
RESTRIÇÃO: impedir que prefixo e id sejam diferentes dos existentes nas tabelas viatura e ocorrencia.

FUNÇÃO: remover_viatura_storage
FAZ: remove uma viatura registrada na tabela viatura
ENTRADA: recebe o prefixo da viatura (str)
SAÍDA: retorna o a quantidade de linhas afetadas
REGRA:
. a função abre a conexão.
. cria o cursor.
. estabele PRAGMA para as chaves estrangeiras.
. executa a exclusão da viatura conforme argumento recebido.
. guarda o contagem de linhas afetadas em uma variável
. envia as alterações
. encerra a conexao
. retorna a variavel com valor da contagem de linhas
EXCEÇÕES: apagar chave que é estrangeira em outra tabela. IntegrityError.

FUNÇÃO: remover_viatura_service
FAZ: recebe prefixo como argumento da interface, chama a função remover_viatura_storage e devolve resultado, em contrato padrão, para a interface.
ENTRADA: argumento prefixo (str)
SAÍDA: resultado em contrato padrão (True, resultado) ou (False, mensagem de erro)
REGRA:
. a função recebe prefixo como argumento
. valida se argumento foi digitado:
.. se errado, retorna (False, "mensagem de erro")
. tentar: chamar função remover_viatura_storage passando prefixo como argumento e atribui o resultado na variável resultado
.. se erro, retorna (False, "mensagem de erro")
. verifica se resultado é 0:
.. se sim, retorna (False, "mensagem de erro")
.. se não, retorna (True, resultado)
EXCEÇÕES: receber erro na tentativa de resultado da chamada de storage.

FUNÇÃO: editar_viatura_storage
FAZ: recebe os argumentos prefixo, quilometragem, estacao, situacao e devolve se houve ou não alteração.
ENTRADA: argumentos prefixo, quilometragem, estacao, situacao
SAÍDA: variavel com resultado de rowncount 1 ou 0
REGRA:
. função recebe os argumentos
. abre conexao
. monta cursor
. executa PRAGMA para chave estrangeira
. executa comando para editar as chaves permitidas
. variavel resultado recebe a contegem de linhas alteradas
. envia a alterações para o banco
. encerra a conexão
. retorna com o a variavel
EXCEÇÕES: valor inaceitável no CHECK da chave situacao. IntegrityError.

FUNÇÃO: editar_viatura_service
FAZ: recebe argumentos da interface, chama a função do storage e retorna contrato padrão para a interface.
ENTRADA: argumentos prefixo, quilometragem, estacao e situacao.
SAÍDA: sucesso (True, resultado) e falha (False, "mensagem de erro")
REGRA:
. receber os argumentos da interface
. verificar se o prefixo não foi preenchido
.. retornar (False, "mensagem de erro")
. verificar se quilometragem não foi preenchido
.. retornar (False, "mensagem de erro")
. verificar se estacao não foi preenchido
.. retornar (False, "mensagem de erro")
. verificar se situacao não foi preenchido
.. retornar (False, "mensagem de erro")
. declarar válidas as situações (operando, manutencao e baixda)
. verificar se situação não está entre as situações validas
.. se sim, retornar (False, "mensagem de erro")
.tentar: declarar variável resultado e atribuir o resultado da função storage com os argumentos prefixo, quilometragem, estacao e situacao
.. se erro IntegrityError, retorna (False, "mensagem de erro")
. verificar se resultado é igual a 0:
.. se sim, retornar (False, "mensagem de erro")
.. se não, retornar (True, resultado)
EXCEÇÕES: prefixo não foi preenchido. IntegrityErro: CHECK da situacao bloqueou entrada errada.

FUNÇÃO: registrar_ocorrencia_storage
FAZ:registra quatro dados - sdo (int), data (str), tipo (str), local (str), descricao (str) - da ocorrencia no banco de dados e retorna
a última linha modificada no banco.
ENTRADA: argumentos - sdo (int), data (str), tipo (str), local (str), descricao (str)
SAÍDA: valor da ultima linha modificada
REGRA: a função abre a conexão executa a inserção dos argumentos que recebeu na tabela e retorna com a última linha
modificada.
EXCEÇÕES: se usuario digitar mesmo sdo e data o banco volta sql.IntegrityError.

FUNÇÃO: registrar_ocorrencia_service
FAZ: recebe 5 campos da interface, valida, chama o storage, traduz o retorno em contrato padrão.
ENTRADA: sdo (int), data (str), tipo (str), local (str), descricao (str)
SAÍDA: (True, id_gerado) ou (False, "mensagem")
REGRA:
. valida se sdo foi preenchido (não é 0/None)
.. se falhar, retorna (False, "mensagem")
. valida se data foi preenchida
.. se falhar, retorna (False, "mensagem")
. valida se tipo foi preenchido
.. se falhar, retorna (False, "mensagem")
. valida se local foi preenchido
.. se falhar, retorna (False, "mensagem")
. valida se descricao foi preenchida
.. se falhar, retorna (False, "mensagem")
. tenta: chama registrar_ocorrencia_storage(sdo, data, tipo, local, descricao), atribui em resultado
.. se sqlite3.IntegrityError: retorna (False, "já existe ocorrência com esse SDO nesta data")
. retorna (True, resultado)
EXCEÇÕES: sqlite3.IntegrityError (violação de UNIQUE composto sdo+data).


FUNÇÃO: listar_ocorrencia_storage
FAZ: recebe a chamada externa e retorna todas as linhas da tabela ocorrencia.
ENTRADA: nenhuma
SAÍDA: lista de tuplas contendo as colunas sdo, data, tipo, local, descricao dentro da variavel resultado.
REGRA:
. abre a conexao
. cria cursor para a conexao
. executa PRAGMA para chaves estrangeiras
. executa SELECT para todos os campos dentro da tabela ocorrencia
. cria variavel resultado e atribui a ela todas as linhas da tabela
. encerra conexao
. retorna a variavel resultado
EXCEÇÕES: não há possibilidade de erros.

FUNÇÃO: listar_ocorrencia_service
FAZ: recebe a chamada da interface, chama o storage, recebe o retorno de storage, valida o retorno de storage e retorna para a interface com (True, dados) ou (False, "mensagem") conforme o contrato já estabelecido. 
ENTRADA: nenhuma
SAÍDA: tupla (True, com a lista de tuplas recebida do storage) ou (False, "mensagem") conforme o contrato.
REGRA:
. recebe a chamada da interface
. declara variável resultado e atribui a ela o retorno do storage
. retornar (True, resultado)
EXCEÇÕES: não há possibilidade de erros.