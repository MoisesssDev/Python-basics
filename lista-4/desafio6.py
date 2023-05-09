# Crie uma lista com o nome de 5 amigos. Imprima o segundo elemento da lista.
# Faça uma repetição para imprimir cinco mensagens, uma para cada amigo, com a seguinte estrutura:
# “Bom dia, Fulano” . Onde Fulano será o nome de cada amigo contido na lista.

lista = ["leandro", "fernando", "ricardo", "Luiza", "Maria"]

print("Segundo elemento da lista: ", lista[1])

for i in range(len(lista)):
    print("Bom dia,", lista[i])