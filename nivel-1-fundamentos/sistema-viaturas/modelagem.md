FUNÇÃO: registrar ocorrência service
FAZ: verifica os dados digitados nos campos, chama a lógica e retorna verdadeiro ou falso para a interface
ENTRADA: lista de ocorrências, lista de viaturas, tipo de ocorrência, local de ocorrência, descrição de ocorrência e prefixo de viatura.
SAÍDA: True com novo dicionário ou False com mensagem de erro.
REGRA:
. verificar se o usuário deixou de digitar algum dos campos.
.. se não, retorna erro e mensagem para a interface.
.. se sim:
... verificar se a viatura digitada existe na lista de viaturas ativas.
....se não, retorna erro e mensagem para a interface.
.... se sim:
.....chama a lógica e atribui o retorno a uma variável.
..... salva a lista de ocorrências.
..... retorna verdadeiro e dicionário para a interface.
EXCEÇÕES: o usuário não digitar nada em qualquer um dos campos e digitar viaturas que não estejam registradas e ativas.
