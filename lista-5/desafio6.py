notas = []


for i in range(1, 6):
    soma = 0
    print("Notas aluno", i)
    for j in range(4):
        nota = eval(input("nota: "))
        soma += nota
    media = soma/4

    notas.append(media)

qtd = 0 
for i in notas:
    if(i >= 7):
        qtd += 1

print(qtd, "notas maior ou igual a 7")