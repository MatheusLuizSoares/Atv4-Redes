listalet = list()

while True:
    n = int(input("Digite um número inteiro e positivo até 999 ou digite 0 para encerrar: "))
    
    if n == 0:
        break
    if 0 < n <= 999:
        tam = int(input("Digite qual posição que o número deve ficar: "))
        if 0 < tam <= 999:
            listalet = [int(i) for i in str(n)]
            print(f"O {tam}º número da lista é: {listalet[tam - 1]}")
            
            consta = int(input("Digite um número que está na lista: "))
            if consta in listalet:
             print(f"O número {consta} está na lista.")
            else:
             print(f"O número {consta} não está na lista.")
             
        else:
         print("A posição do número na lista deve ser entre 1 e 999.")
    else:
     print("O número não corresponde ao intervalo permitido.")


