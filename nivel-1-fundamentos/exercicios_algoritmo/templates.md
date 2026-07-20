"Filtro — Filter""

    Mantém só os itens que passam numa condição. Quantidade de saída ≤ entrada.
    python: list comprehension com filtro

    resultado = [item for item in lista if condição]
    Você usou: [venda for venda in vendas if venda["valor"] * venda["quantidade"] >= 10]

"Transformação — Map"

    Aplica um cálculo/transformação em cada item. 1 entrada → 1 saída.

    python: list comprehension simples

    resultado = [transformação(item) for item in lista]

    # list comprehension construindo dict por item
    resultado = [{"chave_saida_1": chave, "chave_saida_2": valor} for chave, valor in dict.items()]
    Você usou: a transformação dict→lista de dicts é exatamente isto.

"Filtro + Transformação juntos"

    Comprehension aceita os dois na mesma linha.
    pythonresultado = [transformação(item) for item in lista if condição]

    Agrupamento por soma — Group by + Sum
    Junta vários itens com a mesma chave somando um valor. Quantidade de saída < entrada.
    
    python dict-acumulador (soma)
    
    acumulador = {}
    for item in lista:
        chave = item["categoria"]
        valor = item["quanto"]
        if chave not in acumulador:
            acumulador[chave] = 0
        acumulador[chave] += valor
    
    Você usou no exercício de hoje. Nome canônico em EN: "group by" (SQL) ou "reduce by key".

"Agrupamento por contagem — Group by + Count"
    
    Mesma estrutura, mas soma 1 em vez de um valor.
    
    pythonacumulador = {}
    for item in lista:
        chave = item["categoria"]
        if chave not in acumulador:
            acumulador[chave] = 0
        acumulador[chave] += 1

"Agrupamento por média — Group by + Average"
    
    Dois acumuladores paralelos: soma e contagem. Média = soma / contagem no final.
    
    python
    
        soma = {}
        contagem = {}
        for item in lista:
            chave = item["categoria"]
            valor = item["valor"]
            if chave not in soma:
                soma[chave] = 0
                contagem[chave] = 0
            soma[chave] += valor
            contagem[chave] += 1

        media = {chave: soma[chave] / contagem[chave] for chave in soma}

"Ordenação — Sort"
   
    Reordena. Quantidade de saída = entrada.
    
    python: por chave de dict
    sorted(lista, key=lambda x: x["faturamento"], reverse=True)

    . multi-critério
    sorted(lista, key=lambda x: (x["categoria"], -x["faturamento"]))

"Join lógico — Join (por chave compartilhada)"
    
    Cruza duas coleções pela chave que elas têm em comum. Padrão: monta dict de lookup primeiro, depois itera.
    
    python:
    
        1. lookup
            funcionarios_por_id = {f["id"]: f for f in funcionarios}

        2. itera no lado que filtra (filtro implícito) + cruza
            resultado = []
            for s in salarios:
                funcionario = funcionarios_por_id[s["funcionario_id"]]
                resultado.append({"nome": funcionario["nome"], "salario": s["salario"]})
        
    Exercício de ontem.

"Deduplicação — Dedupe"
    
    Remove repetidos. Quantidade de saída ≤ entrada.

    python:
        unicos = set(lista)              # se forem valores simples
        unicos = list(set(lista))        # se precisar voltar pra lista

Tabela-resumo (a mesma da mensagem anterior, agora com nomes EN)
Operação        EN                  Muda quantidade?    Ferramenta
Filtro          Filter              reduz               list comp com if
Transformação   Map                 mantém              list comp
Agrupamento     Group by / Reduce   reduz juntando      dict-acumulador
Ordenação       Sort                mantém              sorted + lambda
Join lógico     Join                depende             dict de lookup + loop
Deduplicação    Dedupe              reduz               set()