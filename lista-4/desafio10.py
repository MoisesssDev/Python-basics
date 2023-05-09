# Crie uma lista com 10 números. Depois solicite ao usuário que digite um número e imprima se o número
# está presente na lista ou não. Para resolver esse problema, percorra a lista e teste cada um dos elementos.
# Caso encontre o elemento, imprima que encontrou e utilize o comando break para sair da repetição.
# Por fim, utilize o comando print(elemento in lista) para averiguar se o resultado é o mesmo.

lista = [23, 34, 13, 67, 8, 12, 3, 78, 91, 10]

n = eval(input("Digite um numero: "))
resposta = False

for i in range(len(lista)):
    if(n == lista[i]):
        print("O numero", n, "existe na lista")
        resposta = True
        break

if(resposta == False):
    print("O numero", n, "nao existe na lista")