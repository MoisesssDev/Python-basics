# Crie um dicionário para armazenar 5 CEPs (chave) e seus respectivos endereços (valor). Tanto o CEP
# quanto o endereço devem ser strings. Utilize a estrutura de repetição while para garantir que cada CEP
# possui tamanho igual a 8 (exemplo: 49060560). Ao final imprima o dicionário.
# obs: Para testar o tamanho do CEP façam o seguinte: if (len (CEP) == 8). Não utilizem hífen.

dicionario = {}

for i in range(5):
    while True:
        cep = input("Digite o CEP: ")
        if (len(cep) == 8):
            break
    endereco = input("Digite seu endereco: ")

    dicionario[cep] = endereco

for i in dicionario:
    print(i,", endereco: ",dicionario[i])