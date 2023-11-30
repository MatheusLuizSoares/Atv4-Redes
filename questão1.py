import random

n = int(input("Digite um valor positivo:"))
if n <= 0:
    print("O número que você digitou é invalido")
else:
    lista = [random.randint(0, 99) for i in range(n)] 
    
    print(f"lista 1 {lista}")
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    print(f"a Lista aleatória foi: {lista}")