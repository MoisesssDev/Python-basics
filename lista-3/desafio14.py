i = 1
maior_valor = 0
soma = 0

while i <= 10:
    valor = int(input("Digite um valor positivo: "))
    if valor < 0:
        print("Valor inválido. Digite um valor positivo.")
    else:
        if valor > maior_valor:
            maior_valor = valor
        soma += valor
        i += 1

media = soma / 10

print("Maior valor digitado:", maior_valor)
print("Soma dos valores digitados:", soma)
print("Média aritmética dos valores digitados:", media)
