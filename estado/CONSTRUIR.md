# CONSTRUIR — agenda-barbearia

<!-- Estado do chat de construção. Abre lendo, fecha atualizando. -->
<!-- Este chat escreve só neste arquivo. Desde 14OUT, absorveu o ESTADO.md antigo, -->
<!-- exceto PRIMM (vive em PRIMM.md) e TREINO (vive em TREINO.md). -->

## ORGANIZAÇÃO (desde 24SET)

3 chats, 1 projeto (agenda-barbearia). Estado em trilha-programacao/estado/,
um arquivo por trilha (desde 14OUT): CONSTRUIR.md, PRIMM.md, TREINO.md,
FUNDAMENTOS.md. Cada chat escreve só no seu.
CONSTRUIR — escreve o agenda-barbearia
PRIMM — lê repositório real e pequeno do GitHub; o engenheiro
pergunta "o que isso faz?" antes de rodar ou mexer
TREINO — exercícios curtos e fechados em
trilha-programacao/nivel-1-fundamentos/exercicios_algoritmo
Construir é o eixo. PRIMM entra antes de cada camada nova.
Treino entra quando um padrão vence ou trava.
Se algum chat abrir projeto próprio, virou a quarta frente parada.

## CICLO

construir: sessão 17, 2026-10-14
(sessões 1 a 12 entre 12SET e 21SET; 13 em 26SET, 14 em 28SET,
15 em 02OUT, 16 em 03OUT, 17 em 14OUT)

## REPOSITÓRIOS

agenda-barbearia — PROJETO ATIVO, desde 14SET26
https://github.com/marVinOliBar/agenda-barbearia
trilha-programacao — 80 commits até 30AGO26. Guarda a pasta estado/ e,
desde 24SET, os exercícios do chat de treino
hello-fastapi (Nditah) — clone local do PRIMM, não é dele
escala-sgb — 4 commits, 14AGO26 a 22AGO26. Parado
sistema-bombeiros-db — dentro de trilha-programacao. Parado, fonte de matéria

## PROJETO

repositório: https://github.com/marVinOliBar/agenda-barbearia
fatia 1: uma entidade, 4 camadas, deploy no Render. Pequeno de propósito:
tem que caber numa reconstrução do zero (etapa Make do PRIMM),
senão é o ciclo antigo com nome novo
Método PRIMM (Sentance & Waite): Predict, Run, Investigate, Modify, Make.
Escopo: ~150 linhas, 5 arquivos.

regras de negócio:
(1) não agendar em horário passado -> service. FEITO [17SET]
(2) horário único -> UNIQUE(inicio) no banco. FEITO

camadas:
schema.sql, criar_banco.py — banco
storage.py — fala com o banco
service.py — regras (criar, listar, formatar, inicio_antes_de_agora)
api.py — GET / (página), GET /agendamentos (dados),
POST /agendamentos (formulário)
templates/index.html — formulário + lista
test_regras.py — 9 testes verdes

último commit: 14OUT, "tela: formulario marca agendamento, redirect 303 para /"

## PRÓXIMO

mostrar o erro dentro da página, em vez do {"detail": ...} cru
depois: deploy no Render

## DECISÕES

IntegrityError sobe do storage; service traduz.
storage = declarar fora de escopo; service = tratar
normalizar na fronteira (service), um lugar só —
regra duplicada é regra que diverge
formatar_agendamentos é função PURA: recebe linhas, não busca no banco.
Foi isso que permitiu testar sem banco. Pode ser revisto, mas não por acaso.
Exclui cancelados (decisão de projeto, pode mudar).
Chave do dicionário: id_cliente (não id)
ValueError de data inválida vira (False, "A data inserida não é real.")
no service; try pequeno só em volta da regra de data [19SET]
inicio_antes_de_agora recebe `agora` (injeção de dependência); o service
chama com datetime.now(). Regra testável sem relógio [21SET]
`<` estrito: now() tem segundos, então marcar no minuto atual é
recusado na prática. Aceito para barbearia [21SET]
endereço da API = substantivo no plural; o verbo HTTP diz a ação.
Fonte: guia de desenho de API da Microsoft (Azure Architecture Center)
API não tem regra: recebe o pedido e passa para o service [26SET]
recusa do service -> HTTPException 400 com detail [02OUT]
página montada no servidor com Jinja2; "/" é a página,
"/agendamentos" são os dados [03OUT]
POST recebe FORMULÁRIO (Form Model + Annotated), não mais JSON;
sucesso devolve 303 para "/" — mesmo desenho do hello-fastapi [14OUT]
REGRA DE DEFEITO [26SET]: defeito vai para a lista e é consertado depois
da fatia 1 no ar. Só na hora se trava o próximo passo ou estraga dado
que não dá para descartar

## DEFEITOS CONHECIDOS

horário duplicado: "08:00", "8:00", "2026-10-1" e espaço sobrando no
fim passam como horários diferentes no UNIQUE. Provado em 26SET (3
clientes no mesmo horário) e visível na tela em 14OUT (2026-09-29 08:00
aparece duas vezes). Conserto: normalizar com strptime -> strftime
erro na tela aparece como JSON cru {"detail": ...}
horário ocupado devolve 400; o preciso é 409. Exige que o service diga
QUAL recusa foi
/docs mostra o 400 como "Undocumented" (a rota só declara 200 e 422)
telefone aceita qualquer texto: o Pydantic confere o TIPO, não o SENTIDO
campo de data é texto. O campo de calendário (datetime-local) manda
"2026-10-21T09:00", com T, e o service recusa como data irreal.
Exemplo de borda entre camadas
banco tem dado velho de antes das regras (sem nome, data passada,
"string"). Fictício: pode apagar agenda.db e rodar criar_banco.py
cupom.py está no repositório — é arquivo de investigação, sai do repo

## PENDENTE

teste do caminho feliz do service — precisa de banco isolado nos testes
(depende do relógio, já resolvido, e do banco)
fuso do servidor no Render — NÃO VERIFICADO. Conferir na sessão do deploy
COMO_RODAR.md na raiz (sugerido em 03OUT): python -m uvicorn api:app --reload

## FORA DE ESCOPO NA FATIA 1 (decisão, 15SET)

sobreposição de intervalos — UNIQUE(inicio) só impede instante idêntico,
não 14:00 × 14:01. Exige duracao ou fim na tabela + consulta de overlap
no service. Grade de horários fixa (14:00, 14:30...) reduziria sobreposição
a igualdade e faria UNIQUE voltar a bastar. Entra na fatia 2 ou 3.

## RÉGUA DE CHEGADA

1 repositório que um estranho clona e roda em 5 min — não (falta README /
COMO_RODAR)
2 sistema no ar com URL real — não. É o alvo da fatia 1. Roda local,
ponta a ponta, desde 14OUT
3 feature inteira formulada e escrita por ele sem consulta — não
4 essa feature explicada em voz alta, em inglês — não

## FUNDAMENTOS

F0 (a) anatomia do traceback — CONSOLIDADO [sessão 2, 13SET]
2/2 na forma difícil (código dele acima e abaixo da biblioteca).
Aplicado sozinho em situação real nas sessões 6, 7, 8 e 11,
e no PRIMM (25SET)
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

F0 (c) doc × fórum × chute — CONSOLIDADO [sessão 10, 18SET]
doc = quem fez, com versão e data. fórum = quem usou, com contraditório
público. chute = sem procedência, inclusive tutorial bonito e
inclusive eu de cabeça
ordem: fórum para achar o NOME, doc para confirmar o FATO
modo de falha do chute: resposta certa para outra pergunta
evidência: busca real por "python strptime documentation" devolveu
7 resultados, 0 oficiais, 1 sobre time.strptime (função diferente de
datetime.strptime)
CORRIGIDO [21SET]: o fórum corrige pouco — pesquisa mostra que só 20,5%
das respostas obsoletas do Stack Overflow são atualizadas. Não existe
aviso automático de obsolescência (eu tinha afirmado sem base)

F1 erro da linguagem — PARCIAL
try/finally: DEIXOU de ser gesto memorizado [sessão 7]. Escolheu deixar
o erro subir e soube dizer por quê
try/except com tipo nomeado: FEITO [sessão 8], com a decisão por trás
except nomeado pega o ramo nomeado e só ele: ValueError e IntegrityError
são ramos separados [sessão 11]
try pequeno, em volta do que pode falhar — não da função inteira
quem levanta não é quem traduz
truthy/falsy — EXPOSTO [sessão 8], COMPLETADO [21SET]
falsy: None e False; zero de qualquer número (0, 0.0, 0j, Decimal(0));
sequência ou coleção vazia ("", (), [], {}, set(), range(0)).
Todo o resto é truthy, inclusive " " e (False, "mensagem").
Fonte: docs.python.org/3/library/stdtypes.html#truth-value-testing
`not cliente` já cobre None — "or None" é no-op
`a or b` devolve um dos operandos, não booleano: a se truthy, senão b.
Daí (x or "").strip()
raise: usado por DECISÃO em 02OUT (HTTPException na API). Ver CONCEITOS

F2 caso de borda — ver seção BORDAS

F3 teste — em treino [sessões 7, 8, 9, 11, 12]
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
ciclo vermelho -> conserta -> verde: 3x na sessão 8, de novo na 11
mudar o TESTE para caber no código só se vale quando a expectativa é
que estava errada, e ele sabe dizer por quê
refatoração = muda estrutura, não comportamento; os testes antigos
verdes são a prova [sessão 12]
PENDENTE: teste que toca banco (isolamento). Contornado na sessão 9
extraindo função pura — contorno melhor que o original

F4 camadas e contrato — em treino, na prática
separar lógica de entrada/saída: a parte com regra fica onde dá
para verificar. É o que logic.py deveria ter sido
função pura recebe, não busca [sessão 9]
injeção de dependência, forma mínima: a função recebe o que antes
buscava (relógio, como o banco na sessão 9) [sessão 12]
API não tem regra: recebe o pedido e passa para o service [sessão 13]
corpo do pedido (request body): os dados vão dentro do envelope;
a ficha (class ... BaseModel) diz o que esperar; o Pydantic é o guarda
que confere o tipo e barra com 422 antes de chegar no service [sessão 14]
/docs e /redoc são criados pelo FastAPI (tutorial First Steps)

F5 padrão profissional — PENDENTE como unidade. 0 de 115 funções com type
hint em trilha-programacao; prontidao.py em escala-sgb tem, e é a
exceção [repo]
EXPOSTO [21SET]: parâmetro fica no def, argumento fica na chamada
(FAQ oficial do Python); valor padrão; type hint é etiqueta — o Python
não confere na execução, quem confere é ferramenta (VS Code, mypy);
Long Parameter List (Fowler): lista longa = função fazendo demais

F6 git — PENDENTE como unidade; usa na prática (clone, add, commit, push,
rm --cached, show HEAD:arquivo)

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
eixo 3 aplicado com cupom.py em 17SET (achou o ValueError de data)

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
VENCERAM na sessão 15 (02OUT). Renovação ficou com o chat de treino

exemplar narrado dado no domínio livros/empréstimos. O exercício paralelo
no domínio dele nunca foi feito.

nota do aluno (12SET): treina pouco e esquece rápido — é o que motivou a
regra de validade do consolidado.

## CONCEITOS DADOS NO CONSTRUIR (sessões 14 a 17)

request body: os dados vão dentro do envelope; a ficha
(class ... BaseModel) diz o que esperar; o Pydantic é o guarda que
confere o tipo e barra com 422 antes do service [28SET]
/docs e /redoc são criados pelo FastAPI (tutorial First Steps) [28SET]
instalar (pip, uma vez no computador) ≠ importar (em cada arquivo) [28SET]
código de resposta: 2xx certo, 4xx culpa do pedido, 5xx culpa do
servidor (MDN). 400 Bad Request, 409 Conflict, 422 do Pydantic [02OUT]
raise usado pela primeira vez, por decisão: HTTPException não se dá
return, se dá raise (doc do FastAPI) [02OUT]
template: página com lacunas preenchida no SERVIDOR pelo Jinja2.
{{ }} escreve valor, {% %} é instrução. for-else trata a lista vazia
(borda do zero). HTML não tem for; o navegador recebe a página pronta
(Ctrl+U mostra) [03OUT]
TemplateResponse(request, name, context). Antes do FastAPI 0.108.0 o
name vinha primeiro — por isso a linha 27 do hello-fastapi quebrava [03OUT]
formulário não manda JSON: Form Model + Annotated (tipo + de onde vem),
exige python-multipart. name do input tem que bater com o campo da
ficha, senão 422 na porta, antes do banco [14OUT]
redirect 303: "gravei, agora vai para /"; o navegador faz o GET
sozinho. Visto no Network do próprio sistema [14OUT]
git: push recusado = o remoto tem commits que a pasta não tem.
Conserto: git pull --rebase, depois git push. "0 insertions" com
"create mode" = arquivo criado vazio [14OUT]

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

## ERROS ATIVOS

nenhum. Autoavaliação e código divergem: ele se declara iniciante e escreveu
storage.py e service.py inteiros sem molde. Calibrar pelo código.
Padrão observado nas sessões 2 e 3: quando ele erra três vezes seguidas,
procurar primeiro a palavra que EU não expliquei.

Erros MEUS já corrigidos [21SET]:
sessão 7: disse que from-import impedia reatribuir storage.CAMINHO_BD.
Falso — a função lê a variável do módulo na hora em que roda
sessão 8: lista de falsy incompleta
sessão 10: afirmei aviso de obsolescência no Stack Overflow sem base
Erro MEU [19SET]: inferi autonomia a partir de commit (regra 1 veio de
molde dado em outro chat). Item 3 da régua continua em "não"

## VOCABULÁRIO DADO

constraint, integrity constraint violation, raise/levantar, signature, raises,
section × entry, e.g. = exemplo e não lista, stdlib × site-packages × projeto,
tabela ≠ planilha, âncora (o que vem depois do #), atributo de exceção,
irmão × ancestral na árvore, edge case, bug × edge case, fronteira,
sqlite_master, DEFAULT × NULL explícito, ISO 8601 ordena lexicograficamente,
migração (pendente), .gitignore, truthy/falsy, função pura, normalizar na
fronteira, N+1 query problem, PRIMM, overlap/sobreposição de intervalos,
injeção de dependência, refatoração, parâmetro × argumento, valor padrão,
type hint, Long Parameter List, strftime, rota, GET/POST,
endereço = substantivo no plural, servidor/uvicorn,
request body, BaseModel, Pydantic, 422, /docs, /redoc, status code, 400,
409, HTTPException, detail, template, Jinja2, TemplateResponse, context,
Form, Annotated, python-multipart, redirect, 303, pull --rebase

## REGRA DE CONDUÇÃO

explicar como para quem tem só o ensino médio [21SET]
toda aula verificada antes: código rodado, doc oficial citada, o não
verificado marcado como tal [21SET]
ler a intenção das perguntas dele, não só o texto
nenhuma palavra em pergunta que não tenha sido apontada na exposição.
Marcus pode parar com "não apresentou" [14SET]
não cobrar caso de borda antes da unidade de bordas [14SET]
não trocar o enunciado no meio do exercício [14SET]
"segue a forma por enquanto" é proibido: se precisa disso, o conceito
não está pronto para entrar [15SET]
previsão só sobre repertório já exposto — cobrar previsão sobre peça
ensinada na mesma mensagem é adivinhação [16SET]
não inferir autonomia a partir de commit [19SET]
molde que é para virar arquivo tem que dizer com todas as letras
"cria este arquivo" [26SET]
PRIMM [25SET]: quebra por versão de biblioteca é conserto do engenheiro,
entregue pronto. Rodar é só rodar e observar. Nunca pedir conserto de
código que ele nunca viu
toda sessão tem produção e termina em commit. Sessão sem commit é falha
minha, e vai escrita aqui [14SET]
fundamentos entram como abertura de 15 min, não como sessão inteira [14SET]
escreve só neste arquivo; FUNDAMENTOS.md não é daqui [14OUT]
