import re
from this import s
from tkinter import S
from variaveis import *
lis_Nordeste=list()

for pos  in range(len(siglas)):
 lis_Nordeste.append([siglas[pos],capitais[pos],populacao[pos]])

print(f"n/{lis_Nordeste}n/")

filtro=lambda c:c [2]>=10000
listne=list (filter(filtro,lis_Nordeste))
print(lis_Nordeste)