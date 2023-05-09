# Algoritmo que leia um número inteiro positivo, calcule e imprima o fatorial deste número.
# Utilize as duas estruturas de repetição (for e while). Não utilize a função math.factorial()

## While
n = eval(input("Digite um numero: "))
contador = 1

resultado = 1

while contador <= n:
    resultado *= contador
    contador += 1

print (resultado)


#For
n = eval(input("Digite um numero: "))
resultado = 1

for i in range(1, n + 1):
    resultado *= i

print(resultado)