valor = 0

while True:
    n = float(input("Digite um valor "))
    if n == 0:
        break
    elif n < 0.01:
        print("esse valor está invalido")
        
    else:
        valor += n

valor100 = int(valor * 100)  
nota = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

print(f"Valor total: {valor:.2f}")

for i in nota: # i = note
 if valor100 >= i:
  valor_notas = valor100 // i
  valor100 -= valor_notas * i
  print(f"{valor_notas} A quantidade é {i / 100:.2f}")