# Ajustar o algoritmo anterior de forma que, além da soma, os números ímpares sejam exibidos.

impares = []
i = 0
aux = 1
while(i < 20):
    if(aux % 2 != 0):
        impares.append(aux)
        i += 1

    aux += 1
    
soma = 0
print("Os 20 primeiros numeros impares: ")
for i in range(len(impares)):
    soma += impares[i]
    print(impares[i])

print("A soma dos 20 primeiros numeros impares: ",soma)

#Confirmação
print(sum(impares))