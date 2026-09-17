# ESTADO.md — formacao-programacao

<!-- Fonte única do estado. Método e piso vivem na skill, não aqui. -->
<!-- Origem de cada linha: [repo] lido do git | [chat] sessão anterior | [assumido] confirmar -->

## CICLO ATUAL

sessoes: 9
ultima_sessao: 2026-09-16 (sessões 3 a 6 em 14SET, 7 em 15SET, 8 e 9 em 16SET)

## REPOSITÓRIOS

agenda-barbearia — PROJETO ATIVO, desde 14SET26
https://github.com/marVinOliBar/agenda-barbearia
trilha-programacao — 80 commits, 16MAR26 a 30AGO26. Parado. Guarda este ESTADO.md
escala-sgb — 4 commits, 14AGO26 a 22AGO26. Parado
sistema-bombeiros-db — dentro de trilha-programacao. Parado, fonte de matéria

## PROJETO ATIVO — agenda-barbearia

Fatia 1: uma entidade, 4 camadas, deploy no Render.
Método PRIMM (Sentance & Waite): Predict, Run, Investigate, Modify, Make.
Escopo: ~150 linhas, 5 arquivos. Pequeno de propósito — tem que caber numa
reconstrução do zero pelo Marcus (a etapa Make), senão é o ciclo antigo com
nome novo.

Regras de negócio:
(1) não agendar em horário passado -> service. PENDENTE
(2) horário único -> UNIQUE(inicio) no banco. FEITO

FEITO: schema.sql, criar_banco.py, .gitignore, storage.py,
service.py (criar + listar + formatar), test_regras.py (4 testes verdes)
PRÓXIMO: regra 1 (traz datetime), depois api.py e index.html

Decisões registradas:
IntegrityError sobe do storage; service traduz.
storage = declarar fora de escopo; service = tratar
Normalizar na fronteira (service), um lugar só —
regra duplicada é regra que diverge
formatar_agendamentos é função PURA: recebe linhas, não busca no banco.
Foi isso que permitiu testar sem banco. Pode ser revisto, mas não por
acaso
formatar exclui cancelados — decisão de projeto, pode mudar
chave do dicionário: id_cliente (não id)

FORA DE ESCOPO NA FATIA 1 (decisão, 15SET):
sobreposição de intervalos — UNIQUE(inicio) só impede instante idêntico,
não 14:00 × 14:01. Exige duracao ou fim na tabela + consulta de overlap
no service. Grade de horários fixa (14:00, 14:30...) reduziria sobreposição
a igualdade e faria UNIQUE voltar a bastar. Entra na fatia 2 ou 3.

## FUNDAMENTOS

F0 (a) anatomia do traceback — CONSOLIDADO [sessão 2, 13SET]
2/2 na forma difícil (código dele acima e abaixo da biblioteca).
Aplicado sozinho em situação real nas sessões 6, 7 e 8
levantada = SEMPRE o último bloco. culpado = último bloco cujo
CAMINHO está dentro do projeto
pré-requisito que faltava: ler caminho de arquivo
(stdlib / site-packages / projeto)

F0 (b) documentação oficial — em treino
firme: página pelo tipo do erro, entrada, âncora
instável: seção × entrada (errou 2 sessões seguidas);
cadeia de subclasses lida de lado, não para cima
entrada pode ter atributos; cadeia para na fronteira do módulo
usar /3/ e não /pt-br/; digitar o endereço, não pesquisar

F0 (c) doc × fórum × chute — PENDENTE
material pronto: busca real por "python strptime documentation"
devolveu 7 resultados, 0 oficiais, 1 sobre time.strptime
(função diferente de datetime.strptime)

F1 erro da linguagem — PARCIAL
try/finally: DEIXOU de ser gesto memorizado [sessão 7]. Escolheu deixar
o erro subir e soube dizer por quê
try/except com tipo nomeado: FEITO [sessão 8], com a decisão por trás
truthy/falsy — EXPOSTO [sessão 8]
falsy: None, "", 0, [], {}. Todo o resto é truthy,
inclusive " " e (False, "mensagem")
`not cliente` já cobre None — "or None" é no-op
`a or b` devolve VALOR, não booleano: a se truthy, senão b.
Daí (x or "").strip()
raise: ainda não precisou DECIDIR usar. A decisão é a matéria

F2 caso de borda — ver seção BORDAS

F3 teste — em treino [sessões 7, 8, 9]
teste = programa que roda teu programa e compara
três partes: preparar, executar, verificar
convenção: arquivo test*\*.py, função test*\*
REGRA: sempre conferir "collected N items". Usada em situação real
na sessão 9 (3 testes comentados, detectados pelo número)
assert precisa COMPARAR. Valor sozinho testa existência, e quase tudo
em Python é verdadeiro. PROVADO NA TELA: 2 testes verdes com o
service destruído
dois sabores de falha:
AssertionError = rodou e não bateu (lógica)
outra exceção = nem chegou ao fim (robustez)
ciclo vermelho -> conserta -> verde: 3x na sessão 8
mudar o TESTE para caber no código só se vale quando a expectativa é
que estava errada, e ele sabe dizer por quê
PENDENTE: teste que toca banco (isolamento). Contornado na sessão 9
extraindo função pura — contorno melhor que o original

F4 camadas e contrato — em treino, na prática
separar lógica de entrada/saída: a parte com regra fica onde dá
para verificar. É o que logic.py deveria ter sido

F5 padrão profissional — PENDENTE. 0 de 115 funções com type hint em
trilha-programacao; prontidao.py em escala-sgb tem, e é a exceção [repo]

F6 git — PENDENTE como unidade; usa na prática

## BORDAS

nivel 0 — EXPOSTO [sessão 4, 14SET]
borda = entrada numa fronteira da função. NÃO é defeito, NÃO é
"retorno inesperado" (o próprio Marcus propôs essa definição e
derrubou-a com contraexemplo)
borda é propriedade da ENTRADA; defeito é propriedade do COMPORTAMENTO
três eixos: quantidade (0/1/muitos, só para COLEÇÃO),
correspondência (tem par / não tem / vários),
valor (vazio, nulo, limite)
três saídas: tratar, recusar, declarar fora de escopo
fronteiras existem sem if no código: laço em 0 voltas,
chave ausente no dicionário, divisão por zero
ENUMERAR é de cabeça (os eixos); TESTAR é na máquina. Dois passos
primeira varredura feita na sessão 5, em código dele

nivel 1 — PENDENTE: os eixos mudam conforme a camada
(lógica pura / storage / API). Sessão inteira.

## PADRÕES

join lógico — degrau 2. Índice de consulta dado em 14SET
dicionário tem dois usos: acumulador (destino) e
índice de consulta (fonte, não cresce, não é percorrido)
regra do join: percorre o lado muitos, indexa o lado um
reaparece na fatia 2, em SQL e em Python lado a lado
N+1 query problem: o nome profissional do que ele aprendeu

filter · dict-acumulador · chave composta · dois acumuladores paralelos ·
group by (count, sum, max, set) · map · sort multi-critério com chave negativa ·
list e dict comprehension
CONSOLIDADOS CONFIRMADOS [sessão 9, 16SET]: comprehension com
desempacotamento + filtro saiu correta de primeira, em código real.
Próxima validade: sessão 15

exemplar narrado dado no domínio livros/empréstimos. O exercício paralelo
no domínio dele nunca foi feito.

nota do aluno (12SET): treina pouco e esquece rápido — é o que motivou a
regra de validade do consolidado.

## DÍVIDAS TÉCNICAS (matéria, não cobrança)

logic.py do sistema-bombeiros-db tem 0 bytes desde o primeiro commit
(16MAR26). A camada lógica imposta como lei não existe; o service valida
direto. Virou matéria na sessão 9 via função pura [repo]
tests/ do sistema-bombeiros-db é script de asserts com sys.path na mão,
não pytest [repo]
teste*sem_ancoras em escala-sgb/tests/test_prontidao.py não roda: prefixo
"teste*" em vez de "test\_". O único teste de borda do projeto nunca
executou. REPRODUZIDO na tela do Marcus na sessão 7 [repo]
registrar_viatura_service rejeita quilometragem 0 com "if not quilometragem".
Confirmado rodando na sessão 5; km=-500 e km="muito" também passam;
SITUACOES_VALIDAS é declarada e nunca usada [repo]
api.py tem um GET /ocorrencia solto, fora da fatia [repo]
data '03/08/2026' no bombeiros.db, misturada com ISO — quebra strptime [repo]

## RÉGUA DE CHEGADA

1 repositório que um estranho clona e roda em 5 min — não (falta README)
2 sistema no ar com URL real — não. É o alvo da fatia 1
3 feature inteira formulada e escrita por ele sem consulta — não
4 essa feature explicada em voz alta, em inglês — não

## ERROS ATIVOS

nenhum. Autoavaliação e código divergem: ele se declara iniciante e escreveu
storage.py e service.py inteiros sem molde. Calibrar pelo código.
Padrão observado nas sessões 2 e 3: quando ele erra três vezes seguidas,
procurar primeiro a palavra que EU não expliquei.

## VOCABULÁRIO DADO

constraint, integrity constraint violation, raise/levantar, signature, raises,
section × entry, e.g. = exemplo e não lista, stdlib × site-packages × projeto,
tabela ≠ planilha, âncora (o que vem depois do #), atributo de exceção,
irmão × ancestral na árvore, edge case, bug × edge case, fronteira,
sqlite_master, DEFAULT × NULL explícito, ISO 8601 ordena lexicograficamente,
migração (pendente), .gitignore, truthy/falsy, função pura, normalizar na
fronteira, N+1 query problem, PRIMM, overlap/sobreposição de intervalos

## REGRA DE CONDUÇÃO

nenhuma palavra em pergunta que não tenha sido apontada na exposição.
Marcus pode parar com "não apresentou" [14SET]
não cobrar caso de borda antes da unidade de bordas [14SET]
não trocar o enunciado no meio do exercício [14SET]
"segue a forma por enquanto" é proibido: se precisa disso, o conceito
não está pronto para entrar [15SET]
previsão só sobre repertório já exposto — cobrar previsão sobre peça
ensinada na mesma mensagem é adivinhação [16SET]
toda sessão tem produção e termina em commit. Sessão sem commit é falha
minha, e vai escrita aqui [14SET]
fundamentos entram como abertura de 15 min, não como sessão inteira [14SET]
