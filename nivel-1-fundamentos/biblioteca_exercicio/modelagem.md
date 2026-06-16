INTERFACE
Objetivo: Registrar livros com título e autor
FUNÇÃO: registrar
FAZ: interage com o usuário que deseja registrar um livro na biblioteca
ENTRADA: lista de dicionários livros
SAÍDA: imprime saída de sucesso ou falha
REGRA:
. ler o título do livro
. ler o autor do livro
. receber do service o resultado:
.. se sucesso, exibir mensagem de confirmação
.. se falha, exibir a mensagem de erro
EXCEÇÕES: não há

SERVICE
Objetivo: Registrar livros com título e autor
FUNÇÃO: registrar_service.
FAZ: validar as entradas do usuário, chama lógica para tratar dados, chama storage para salvar dados
ENTRADA: livros, título, autor.
SAÍDA: resultado sucesso com dados ou resultado fracasso com mensagem de erro.
REGRA:
.verifica se autor não foi digitado
.. se sim, retorna falha + mensagem
.verifica se livro não foi digitado
.. se sim, retorna falha + mensagem
.itera dentro da lista e:
. verfica se autor e livro digitado já existe dentro de algum dicionário
..se sim, retorna falha + mensagem
. chama a função da lógica e passa a lista e as variáveis
. recebe resultado da lógica
. anexa o resultado a lista livros
. chama storage para salvar a lista atualizada
. retorna sucesso + mensagem para a interface
EXCEÇÕES:título vazio, autor vazio, livro duplicado (mesmo título + mesmo autor).

LOGICA
Objetivo: Registrar livros com título e autor
FUNÇÃO: adicionar
FAZ: adiciona um novo dicionário com título e autor
ENTRADA: título + autor
SAÍDA: dicionário contendo título e autor
REGRA:
. insere título em um dicionário
. insere autor no mesmo dicionário
. retorna dicionário para service
EXCEÇÕES: não há

STORAGE
Objetivo: Salvar a lista livros
FUNÇÃO: salvar
FAZ: salva a lista livros na memória ROM
ENTRADA: lista livros
SAÍDA: não há
REGRA:
. lê a lista livros
. salva os dados em um arquivo .json formatado
EXCEÇÕES: não há

FUNÇÃO: carregar
FAZ: carrega a lista livros salva ou uma vazia
ENTRADA: nenhuma
SAÍDA: lista livros salva ou uma vazia
REGRA:
.tenta ler uma lista livros salva na memória ROM
..e carregar a lista salva
..se o arquivo estiver corrompido ou não houver lista salva
..carrega lista livros nova
EXCEÇÕES: não haver lista salva ou arquivo .json corrompido
