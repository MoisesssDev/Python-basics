# Crie uma lista com 10 números, calcule e exiba a soma dos quadrados dos elementos da lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somaQuadrados = 0


for i in lista:
    somaQuadrados += i * i

print (somaQuadrados)