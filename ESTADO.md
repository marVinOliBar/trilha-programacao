# ESTADO.md — formacao-programacao

<!-- Fonte única do estado. Método e piso vivem na skill, não aqui. -->
<!-- Origem de cada linha: [repo] lido do git | [chat] sessão anterior | [assumido] confirmar -->

## CICLO ATUAL

inicio: 2026-09-12
sessoes: 0
ultima_sessao: —
alvo do ciclo: F0, F1 e F2 dadas; bordas no nível 2; join lógico em folha em branco
revisao: na sessão 12

## REPOSITÓRIOS

trilha-programacao — 80 commits, 16MAR26 a 30AGO26 [repo]
escala-sgb — 4 commits, 14AGO26 a 22AGO26 [repo]

## MODO CORRENTE

DRILL: exercícios 1 a 27 em nivel-1-fundamentos/exercicios_algoritmo [repo]
CONSTRUÇÃO: fatia "registrar atendimento" em sistema-bombeiros-db — aberta [chat 03SET]
feito: buscar_id_ocorrencia_storage (traduz sdo+data no id da FK) [repo 30AGO]
parado em: o service do atendimento, não escrito [repo]
último conceito exposto: chave natural × chave substituta [chat 03SET]

## FUNDAMENTOS

F0 ler erro e documentação — PENDENTE. Declarado por ele em 12SET: não sabe ler
documentação. A skill antiga registrava o oposto como hábito consolidado, e
por isso a lacuna ficou invisível [chat 12SET]
F1 erro da linguagem — PENDENTE, e menor do que o código sugere [chat 12SET]
try/finally: gesto memorizado para fechar conexão, dez vezes no mesmo
contexto, sem transferência para outra situação
IntegrityError: sabe que existe, não tem na ponta da língua, não conhece os
tipos — depende de F0 para investigar
raise: exposto uma vez, nunca precisou DECIDIR quando usar. Não consolidado.
A decisão é a matéria, não a sintaxe
F2 caso de borda — PENDENTE. É o pré-requisito oculto que travou o antigo campo
EXCEÇÕES da modelagem por meses [chat 12SET]
F3 teste — PENDENTE [repo]
F4 camadas e contrato — PENDENTE como unidade; cobrado como lei desde 16MAR [repo]
F5 padrão profissional — PENDENTE. 0 de 115 funções com type hint em
trilha-programacao; prontidao.py em escala-sgb tem, e é a exceção [repo]
F6 git — PENDENTE como unidade; usa branch, merge, resolve conflito e
.gitignore na prática [repo]

## ESCADA DE BORDAS

nível: 0 [assumido]
evidência a favor de 1: os testes existentes cobrem borda de verdade — SDO vazio,
SDO duplicado, virada de ano, data anterior à âncora, dict vazio. Mas todas essas
bordas foram apontadas pelo instrutor, não levantadas por ele [chat/repo]
A primeira sessão de F2 calibra; errar para baixo custa uma sessão.

## PADRÕES

consolidado com validade — produção autônoma verificada, retenção não aferida [repo/chat]
filter · dict-acumulador · chave composta · dois acumuladores paralelos ·
group by (count, sum, max, set) · map · sort multi-critério com chave negativa ·
list e dict comprehension
última aparição: ex27, 29AGO26. Vencem na sessão 6 se não reaparecerem.
em treino — join lógico, degrau 1, 1 sessão [chat 02SET]
exemplar narrado dado no domínio livros/empréstimos (índice, group by sum,
map+join, sort). O exercício paralelo no domínio dele nunca foi feito.
Prazo estoura na sessão 3.
nota do aluno (12SET): treina pouco e esquece rápido — é o que motivou a regra
de validade do consolidado.

## DÍVIDAS TÉCNICAS (matéria, não cobrança)

logic.py do sistema-bombeiros-db tem 0 bytes desde o primeiro commit (16MAR26),
último toque em 20JUN26. A camada lógica imposta como lei não existe; o service
valida direto. É do projeto antigo — o escala-sgb (14AGO26) já nasceu com
domínio de pé. Decisão pendente dele, sem prazo: ou a camada nasce ali, ou a
doutrina passa a dizer três camadas naquele projeto [repo]
tests/ do sistema-bombeiros-db é script de asserts com sys.path na mão, não
pytest; escala-sgb tem pytest.ini e é onde F3 deve acontecer [repo]
teste*sem_ancoras em escala-sgb/tests/test_prontidao.py não roda: prefixo
"teste*" em vez de "test\_", pytest não coleta. O único teste de borda do
projeto nunca executou [repo]
registrar_viatura_service rejeita quilometragem 0 com "if not quilometragem" —
zero é valor legítimo. Material de F2, fonte (b) [repo]
api.py tem um GET /ocorrencia solto, fora da fatia [repo]

## RÉGUA DE CHEGADA

1 repositório que um estranho clona e roda em 5 min — não [repo: sem README de execução]
2 sistema no ar com URL real — não
3 feature inteira formulada e escrita por ele sem consulta — não
4 essa feature explicada em voz alta, em inglês — não

## ERROS ATIVOS

nenhum registrado. Autoavaliação e código divergem: ele se declara iniciante e
produz agregação de quatro operações sem travar. Calibrar pelo código. [chat]
