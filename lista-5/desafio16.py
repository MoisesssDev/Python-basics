# Crie um dicionário para armazenar 2 matrículas (chave) e o respectivo nome (valor) do aluno. Para
# matrícula utilize um número inteiro com no máximo 3 dígitos (menor que 1000). Para o nome utilize string.
# Por fim, imprima o nome do aluno utilizando o get(), passando como parâmetro uma das duas matrículas.
# Ou seja: “print (dicionario.get(alguma_matrícula))”

dicionario = {}

for i in range(2):
    while True:
        matricula = eval(input("Digite a matricula: "))
        if(matricula < 1000):
            break
    nome = input("Digite o nome: ")

    dicionario[matricula] = nome

consulta = eval(input("Qual matricula vc quer consultar: "))

print(dicionario.get(consulta))