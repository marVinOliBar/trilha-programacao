## vindo do CONSTRUIR (sessões 14 a 17)

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

vocabulário: request body, BaseModel, Pydantic, 422, /docs, /redoc,
  status code, 400, 409, HTTPException, detail, template, Jinja2,
  TemplateResponse, context, Form, Annotated, python-multipart,
  redirect, 303, pull --rebase