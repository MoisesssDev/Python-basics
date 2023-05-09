# Crie uma lista com 4 notas. Faça um programa que exiba as notas (uma de cada vez) e a média.
# Utilize o comando print(sum (lista)/len(lista)) para averiguar se o resultado da média está correto.

notas = [7.8, 5.4, 8.9, 9.3]
soma = 0

for i in range(len(notas)):
    soma += notas[i]
    print(i + 1,"a nota:", notas[i])

print("A media é: ", soma/len(notas))

#Correção
print(sum(notas)/len(notas))