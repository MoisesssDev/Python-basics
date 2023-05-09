# Escrever algoritmo para calcular o somatório dos n primeiros múltiplos de 3 maiores que 0.
# Escreva também todos os múltiplos de 3 que fizeram parte do somatório. Utilize o while e o for.
n = eval(input("informe um numero: "))
while n < 0:
    n = eval(input("informe um numero maior que 0: \n"))

i = 1
aux = 3
soma = 0
print("-----------WHILE-------------------")
print("Os ", n, " multiplos de 3 sao: \n")
while i <= n:
    if(aux % 3 == 0):
        print(aux, end=", ")
        soma += aux
        i += 1
    aux += 3

print("soma dos multiplos de 3 = ", soma, "\n")

soma = 0
aux = 3
print("-----------FOR-------------------")
print("Os ", n, " multiplos de 3 sao: \n")
for i in range(n):
    if(aux % 3 == 0):
        print(aux, end=", ")
        soma += aux
    aux += 3

print("soma dos multiplos de 3 = ", soma, "\n")