# Crie uma lista vazia e escreva um algoritmo que insira nessa lista os números pares de 0 a 100.
# Utilize uma das estruturas de repetição. Ao final imprima a lista (print(pares)) para conferir.
lista = []

i = 0

while(i <= 100):
    lista.append(i)
    i += 2

print(lista)