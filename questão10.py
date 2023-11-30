import random
n = int(input("Digite a dimensão da lista: "))

lista = []
for i in range(n):
    lista.append(random.randint(1, 60))
lista_combinacoes = []
for i in range(n):
 for j in range(i+1, n):
  for k in range(j+1, n):
   for l in range(k+1, n):
    for m in range(l+1, n):
     for o in range(m+1, n):
      lista_combinacoes.append([lista[i], lista[j], lista[k], lista[l], lista[m], lista[o]])
      
total_combinacoes = len(lista_combinacoes)
probabilidade_sena = 1 / total_combinacoes
probabilidade_quina = 6 * probabilidade_sena
probabilidade_quadra = 15 * probabilidade_sena
print(f"Lista gerada: {lista}")
print(f"Lista de todas as combinações possíveis é: {lista_combinacoes}")
print(f"Probabilidade de acertar a sena é: {probabilidade_sena:.9f}")
print(f"Probabilidade de acertar a quina é: {probabilidade_quina:.9f}")
print(f"Probabilidade de acertar a quadra é: {probabilidade_quadra:.9f}")
