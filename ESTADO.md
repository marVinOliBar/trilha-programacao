# ESTADO.md — formacao-programacao

<!-- Fonte única do estado. Método e piso vivem na skill, não aqui. -->
<!-- Origem de cada linha: [repo] lido do git | [chat] sessão anterior | [assumido] confirmar -->

## CICLO ATUAL

sessoes: 7
ultima_sessao: 2026-09-15

## REPOSITÓRIOS

trilha-programacao — 80 commits, 16MAR26 a 30AGO26 [repo]
escala-sgb — 4 commits, 14AGO26 a 22AGO26 [repo]
agenda-barbearia — projeto ativo

## FUNDAMENTOS

F0 (b) documentação oficial — em treino
firme: página pelo tipo do erro, entrada, âncora
instável: seção × entrada (2 sessões seguidas);
cadeia de subclasses lida de lado, não para cima
novo: entrada pode ter atributos; cadeia para na
fronteira do módulo
F0 (c) doc × fórum × chute — PENDENTE
F1 erro da linguagem — PENDENTE, e menor do que o código sugere [chat 12SET]
try/finally: gesto memorizado para fechar conexão, dez vezes no mesmo
contexto, sem transferência para outra situação
IntegrityError: sabe que existe, não tem na ponta da língua, não conhece os
tipos — depende de F0 para investigar
raise: exposto uma vez, nunca precisou DECIDIR quando usar. Não consolidado.
A decisão é a matéria, não a sintaxe
F2 caso de borda — PENDENTE. É o pré-requisito oculto que travou o antigo campo
EXCEÇÕES da modelagem por meses [chat 12SET]
F3 teste — nível 0 EXPOSTO [sessão 7, 15SET]
teste = programa que roda teu programa e compara
três partes: preparar, executar, verificar
assert mostra saiu × esperado × origem
convenção: arquivo test*\*.py, função test*\*
REGRA: sempre conferir "collected N items"
nome errado = 0 coletados, sem aviso, suíte verde
reproduzido na tela: é o defeito do escala-sgb
PENDENTE: teste que toca banco (isolamento, tmp_path)
— assunto próprio, não embutir em aula de teste
F4 camadas e contrato — PENDENTE como unidade; cobrado como lei desde 16MAR [repo]
F5 padrão profissional — PENDENTE. 0 de 115 funções com type hint em
trilha-programacao; prontidao.py em escala-sgb tem, e é a exceção [repo]
F6 git — PENDENTE como unidade; usa branch, merge, resolve conflito e
.gitignore na prática [repo]

## PENDENTE DE FUNDAMENTO

F0(c) doc × fórum × chute — abertura de sessão, 15 min
bordas nível 1 (camadas) — abertura de sessão

## BORDAS

nivel 0 — EXPOSTO [sessão 4, 14SET]. Sem exercício ainda.
borda = entrada numa fronteira da função (não é defeito,
não é "retorno inesperado")
três eixos: quantidade (0/1/muitos), correspondência
(tem par / não tem / vários), valor (vazio, nulo, limite)
três saídas: tratar, recusar, declarar fora de escopo
fronteiras existem sem if no código: laço em 0 voltas,
chave ausente no dicionário, divisão por zero
nivel 1 — PENDENTE: os eixos mudam conforme a camada
(lógica pura / storage / API). Sessão inteira.

## PADRÕES

join lógico — degrau 2. Índice de consulta dado em 14SET.
dicionário tem dois usos: acumulador (destino) e
índice de consulta (fonte, não cresce, não é percorrido)
regra do join: percorre o lado muitos, indexa o lado um
filter · dict-acumulador · chave composta · dois acumuladores paralelos ·
group by (count, sum, max, set) · map · sort multi-critério com chave negativa ·
list e dict comprehension
consolidados — VENCIDOS, não reapareceram na sessão 7.
reaparecem no service.py (comprehension e filter)

exemplar narrado dado no domínio livros/empréstimos (índice, group by sum,
map+join, sort). O exercício paralelo no domínio dele nunca foi feito.

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

## VOCABULÁRIO DADO

constraint, integrity constraint violation, raise/levantar,
signature, raises, section × entry, e.g. = exemplo e não lista,
stdlib × site-packages × projeto, tabela ≠ planilha
âncora (o que vem depois do #), seção × entrada, atributo de exceção, irmão × ancestral na árvore
edge case, bug × edge case, fronteira
sqlite_master, DEFAULT × NULL explícito, ISO 8601 ordena
lexicograficamente, migração (pendente), .gitignore

## REGRA DE CONDUÇÃO (14SET)

nenhuma palavra em pergunta que não tenha sido apontada
na exposição. Marcus pode parar com "não apresentou".
não cobrar caso de borda antes da unidade de bordas.
não trocar o enunciado no meio do exercício.

## PROJETO ATIVO — agenda-barbearia

repo: https://github.com/marVinOliBar/agenda-barbearia
FEITO: schema.sql, criar_banco.py, .gitignore,
storage.py, test_regras.py
decisão: IntegrityError sobe do storage; service traduz
storage = declarar fora de escopo; service = tratar
PRÓXIMO: service.py — as duas regras + capturar
IntegrityError e devolver (False, mensagem)

## ERRO MEU (15SET)

empilhei 7 conceitos em 2 mensagens em F3.
"segue a forma por enquanto" é proibido: se precisa
disso, o conceito não está pronto para entrar.
