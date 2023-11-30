gabarito = ['A', 'C', 'B', 'A', 'E', 'D', 'D', 'C', 'A', 'A']
lista_alunos = [
    ['Aluno 01', 'B', 'D', 'E', 'E', 'C', 'D', 'A', 'B', 'C', 'D'],
    ['Aluno 02', 'C', 'D', 'A', 'B', 'D', 'A', 'A', 'C', 'B', 'E'],
    ['Aluno 03', 'A', 'A', 'B', 'D', 'C', 'E', 'E', 'A', 'A', 'C'],
    ['Aluno 04', 'B', 'B', 'C', 'C', 'D', 'E', 'D', 'D', 'E', 'E'],
    ['Aluno 05', 'B', 'B', 'D', 'A', 'A', 'E', 'B', 'D', 'E', 'C'],
    ['Aluno 06', 'C', 'C', 'D', 'E', 'B', 'B', 'C', 'D', 'E', 'A'],
    ['Aluno 07', 'B', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'A', 'B'],
    ['Aluno 08', 'D', 'E', 'A', 'B', 'B', 'C', 'C', 'D', 'A', 'A'],
    ['Aluno 09', 'A', 'A', 'A', 'C', 'B', 'D', 'D', 'E', 'D', 'C'],
    ['Aluno 10', 'B', 'B', 'D', 'E', 'C', 'D', 'C', 'E', 'B', 'A']
]

lista_gabarito = gabarito


lista_provas=list()
for aluno in lista_alunos:
    nome = aluno[0]
    respostas = aluno[1:]
    acertos = sum([1 for i in range(10) if respostas[i] == gabarito[i]])
    lista_provas.append([nome] + respostas + [acertos])

print("Gabarito: ", lista_gabarito)
print("")

print("Lista de alunos:")
for aluno in lista_provas:
    print(f"Nome: {aluno[0]}")
    print(f"Respostas: {aluno[1:11]}")
    print(f"Nota: {aluno[11]}")
    print("")


lista_provas.sort(key=lambda x: x[11], reverse=True)


for aluno in lista_provas:
    print(f"Nome: {aluno[0]}")
    print(f"Respostas: {aluno[1:11]}")
    print(f"Nota: {aluno[11]}")
    print("")
