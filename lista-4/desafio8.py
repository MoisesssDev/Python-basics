# Escreva um algoritmo que armazena em uma lista os 20 primeiros números ímpares maiores que zero.
# Depois, percorra a lista e efetue a soma desses números. Por fim, imprima a soma dos números.
# Utilize o comando print(sum (lista)) para averiguar se o resultado da soma está correto.

impares = []
i = 0
aux = 1
while(i < 20):
    if(aux % 2 != 0):
        impares.append(aux)
        i += 1

    aux += 1
    
soma = 0
for i in range(len(impares)):
    soma += impares[i]

print("A soma dos 20 primeiros numeros impares: ",soma)

#Confirmação
print(sum(impares))