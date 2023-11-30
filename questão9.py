import random

m = int(input("Digite a quantidade de listas na matriz: "))
n = int(input("Digite a quantidade de elementos em cada lista: "))

matriz = [[random.randint(0, 99) for j in range(n)] for i in range(m)]
print("Matriz original:")
for linha in matriz:
  print(linha)


matriz_transposta = [[matriz[j][i] for j in range(m)] for i in range(n)]
print("Matriz transposta:")
for linha in matriz_transposta:
  print(linha)
