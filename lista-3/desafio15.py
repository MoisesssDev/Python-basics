primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor (maior que o primeiro): "))

while segundo_valor <= primeiro_valor:
    print("O segundo valor deve ser maior que o primeiro.")
    segundo_valor = int(input("Digite o segundo valor novamente (maior que o primeiro): "))

print("Os valores digitados foram:", primeiro_valor, "e", segundo_valor)
