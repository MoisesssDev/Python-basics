# 13) Faça um programa que leia 20 números (digitados pelo usuário) e armazene-os em uma lista.
# Armazene os números pares na lista par e os números ímpares na lista ímpar. Imprima as 3 listas.

i = 1
lista = []

while i <= 20:
    lista.append(eval(input('Informe um número inteiro : ')))
    i += 1

pares = []
impares = []

for i in range(len(lista)):
    if(lista[i] % 2 == 0):
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(lista)
print(pares)
print(impares)