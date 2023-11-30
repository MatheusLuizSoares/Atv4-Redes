x = int(input('Informe a quantidade de elementos na lista: '))

lista = list()

for i in range(x):
    n = int(input('Informe um valor: '))
    lista.append(n)
    lista.sort()
    print(lista)
    if n == 0:
     break
    if n > x:
     if len(lista) + 1 > x:
       del lista[-1]
