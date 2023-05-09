# Escreva um programa que, a partir de um dicionário vazio, armazene, neste, uma agenda de tamanho n,
# com n digitado pelo usuário. A agenda consiste de dois campos: nome e telefone. Ou seja, o usuário vai
# digitar (um a um) cada par: nome e telefone. Utilize string tanto para o nome, quanto para o telefone.
# Por fim imprima todos os contatos (nome e telefone).
# obs: Uma vez lidas as variáveis (nome e telefone), faça: dicionario[nome] = telefone.

dicionario = {}

n = eval(input("Digite quantos contatod deseja salvar: "))

for i in range(n):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")

    dicionario[nome] = telefone

for i in dicionario:
    print(i, ": ", dicionario[i])