
from variaveis import *
lis_Nordeste=list()

for pos  in range(len(siglas)):
 lis_Nordeste.append([siglas[pos],capitais[pos],populacao[pos]])

print(f"/n{lis_Nordeste}/n")

lis_Nordeste.sort(key=lambda c:c[2], reverse=True)
print(f"n/ {lis_Nordeste}n/")