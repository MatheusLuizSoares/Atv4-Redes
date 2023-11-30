import random

n = int(input("Digite a dimensão da lista: "))
if n<=0:
 print("o ´numero precisa está entre 0 e 99")
else:
 lista = [random.randint(0, 99) for i in range(n)]

 lista_ordenada = sorted(lista)
if n % 2 == 0:
    mediana = (lista_ordenada[n//2 - 1] + lista_ordenada[n//2]) / 2
else:
 mediana= (lista[n//2])
 media=0
variancia =0

for i in lista:
    media+=1
mdeia=media/n
for i in lista:
    variancia+=((1-media)**2/n)
desvio_padrao = variancia ** 0.5

print(f"Lista gerada é: {lista}")
print(f"Média é: {media}")
print(f"Mediana é: {mediana}")
print(f"A Variância populacional é: {variancia}")
print(f"A Desvio-padrão populacional  é: {desvio_padrao}")
