# 12) Crie um dicionário com seus dados: nome, idade, telefone, endereço. Por fim, imprima um a um todos os
# dados do dicionário, ou seja, a chave e o valor . “nome: fulano”, “idade: 20” ...

dicionario = {
    "nome": "Moises",
    "idade": "21",
    "telefone": "7989899786",
    "endereco": "rua 11, eduardo gomes"
}

for i in dicionario:
    print(i, dicionario[i])
