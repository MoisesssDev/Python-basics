# Crie duas listas, uma se chamará “nomes” e a outra “medias” → nomes = [] medias = []
# O seu programa deve inserir, nessas duas listas, os nomes e as médias de n alunos.
# Para tal, faça um loop (de tamanho n, repete-se n vezes) onde teremos:

# media = 0
# nomes.append (nome lido) # leia nome com input()
# e dentro deste loop, um outro um outro loop (repete-se 3 vezes), onde:
# media = media + nota lida # leia nome com eval (input())

# Fora desse 2° loop, mas ainda dentro do 1° loop, teremos: medias.append(media/3)
# Por fim, fora dos dois loops, imprima os dados inseridos, para cada aluno, utilizando os seguintes comandos:

# for i in range(n):
# print ('Aluno', nomes[i], 'obteve a média', medias[i])

print ('Cadastrar N alunos: nome, 3 notas e a média de cada um\n')

nomes  = []
medias = []   
qtd = eval(input('Informe a quantidade de Alunos : '))

for i in range(qtd): 	# loop dos alunos
   nome = input('Informe o nome do aluno : ')
   nomes.append (nome)
   media = 0
   for j in range(3): #  loop das 3 notas
      media = media + eval(input('Digite a nota : '))
   media = media/3
   medias.append(media)

print ('--------  Resultado ---------\n')
for i in range(qtd):
   print ('Aluno', nomes[i], 'obteve a média', medias[i])