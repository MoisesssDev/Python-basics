n = eval(input("Digite um numero: "))

soma = 0

for i in range(n):
    x = eval(input("informe um novo numero: "))
    soma += x

print(soma/n)