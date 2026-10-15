# PRIMM — estado

<!-- Escrito só pelo chat de PRIMM. Lê CONSTRUIR.md para saber a próxima camada. -->

repositório: Nditah/hello-fastapi — clone em C:\dev\hello-fastapi (casa e serviço), venv próprio
conserto fixo após clonar (linha 27 do app.py):
return templates.TemplateResponse(req, "base.html", {"todo_list": todos})
objetivo: explicar em voz alta o caminho de um clique (tela → API → banco → tela)
e preparar a próxima camada do construir

## SESSÕES

1 [25SET] P da tela; R com quebra na linha 27 (versão do Starlette)
2 [29SET] I do Add, passos 1→2: Network + terminal. Previu certo que trocar
name="title" quebra o /add (422, nada gravado)
3 [05OUT] Update: leu a linha 40 sozinho. /update/999 — previu 404, deu 500
(AttributeError: 'NoneType' object has no attribute 'complete')

## PRÓXIMO

F0(b): entrada do AttributeError na doc oficial (página, entrada, âncora)
M: /update/999 responder 404 — prepara os códigos de erro do construir
PENDENTE: prever cinza→verde — FEITO na sessão 3
BAIXA PRIORIDADE: I do Add, passos 2→3 (SQLAlchemy; o projeto usa sqlite3)

## LIÇÕES

404 é decisão escrita no código; 500 é acidente que ninguém tratou
o navegador só enxerga pedido e resposta (Network); o servidor registra o
mesmo do outro lado (terminal)
tela→API se liga por nomes que batem: action↔rota, method↔get/post,
name↔parâmetro

## EXPOSTO (não cobrar como consolidado)

request, GET×POST, rota, decorator, path parameter, status HTTP
(200/303/404/422/500), Size, Form(...) = obrigatório,
atributo (o ponto faz o papel do colchete do dict), None vindo do .first()
sob pressão na sessão 1: hashable, signature, keyword argument, context do template

## REGRAS DE CONDUÇÃO

quebra por versão de biblioteca é conserto do engenheiro, entregue pronto;
rodar é só rodar e observar
nunca pedir conserto de código que ele nunca viu
pergunta concreta (sim/não + porquê) funciona; pergunta aberta de mapeamento trava
expor antes de perguntar, inclusive sintaxe nova (o ponto, o {{ }})
com código claro, prever é ler — a previsão rende onde o código surpreende

## AMBIENTE

PowerShell: .\venv\Scripts\python -m uvicorn app:app --reload → http://127.0.0.1:8000
VS Code: interpretador do venv (sintoma de errado: import "could not be resolved")
Git Bash: / separa pastas, \ é escape
o clone não é dele: commit fica local, push sempre recusado;
desfazer commit: git reset --soft HEAD~1
