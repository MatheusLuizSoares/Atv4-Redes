from questão7_complemento import*
listcota=cotacoes_dolar 

    # ... e assim por diante


maior_cotacao_por_mes = []
for mes in set(cotacao['mes'] for cotacao in listcota):
    cotacoes_do_mes = [c for c in listcota if c['mes'] == mes]
    maior_cotacao = max(cotacoes_do_mes, key=lambda x: x['cotacao_venda'])
    maior_cotacao_por_mes.append([maior_cotacao['mes'], maior_cotacao['cotacao_venda'], maior_cotacao['data']])

# Montar a segunda lista com a média das cotações de venda de cada mês
media_cotacoes_por_mes = []
for mes in set(cotacao['mes'] for cotacao in listcota):
    cotacoes_do_mes = [c for c in listcota if c['mes'] == mes]
    media_cotacao = sum(c['cotacao_venda'] for c in cotacoes_do_mes) / len(cotacoes_do_mes)
    media_cotacoes_por_mes.append([mes, media_cotacao])

# Exibir as listas resultantes
print("Maior cotação de venda por mês:")
print(maior_cotacao_por_mes)

print("\nMédia das cotações de venda por mês:")
print(media_cotacoes_por_mes)
