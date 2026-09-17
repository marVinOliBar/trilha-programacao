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
    inclusive "   " e (False, "mensagem")
    `not cliente` já cobre None — "or None" é no-op
    `a or b` devolve VALOR,