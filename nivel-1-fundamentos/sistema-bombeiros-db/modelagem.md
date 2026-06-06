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
