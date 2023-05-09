# Faça um programa que insira, em uma lista, 10 números digitados pelo usuário. Depois percorra a lista
# de “trás para frente” e mostre os números na ordem inversa a ordem em que foram inseridos na lista.
# Por fim, utilize os comandos lista.reverse() e print (lista) e veja se o resultado confere.
# A função reverse() inverte a ordem dos elementos.
i = 1
lista = []

while i <= 10:
    n = eval(input("Digite o numero: "))
    lista.append(n)

    i += 1

i = len(lista)
listaReversa = []

while i > 0:
    i -= 1
    listaReversa.append(lista[i])
   

print(lista)
print(listaReversa)
