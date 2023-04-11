n = int(input("Digite um número inteiro positivo menor que 50: "))

while n <= 0 or n >= 50:
    print("Número inválido. Digite um número inteiro positivo menor que 50.")
    n = int(input("Digite um número inteiro positivo menor que 50: "))

soma = 0

for i in range(1, n+1):
    soma += i/(i+1)

print("A soma dos", n, "primeiros termos da sequência é:", round(soma, 2))
