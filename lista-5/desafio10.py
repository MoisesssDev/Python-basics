# Imprima os números repetidos da lista_1. Para fazer isso, crie uma lista_2 vazia. Depois, percorra a
# lista_1 para encontrar os números repetidos. Ao passo que, se um número for repetido e não estiver na
# lista_2, então esse número será adicionado a lista_2. Ao término imprima lista_2 que irá conter apenas os
# números repetidos.

lista_1 = [1, 3, 6, 3, 4, 6, 8, 8, 1, 8, 9, 11, 7, 5]
lista_2 = []

for i in lista_1:
   if (lista_1.count(i) > 1) and (i not in lista_2) :
      lista_2.append(i)
      
print(lista_2)