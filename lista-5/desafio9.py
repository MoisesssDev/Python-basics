# Utilizando duas listas, escreva um programa que armazena e imprima 5 perguntas sobre um crime:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"

# Na lista perguntas armazene as cinco perguntas.
# Na lista respostas armazene as respostas, de modo que cada resposta será: sim ou não.
# Depois verifique quantas respostas iguais a “sim” constam na lista respostas.
# No final o programa deve emitir uma classificação sobre a participação do crime.
# Se houver a resposta “sim” a 2 perguntas, a classificação deve ser "Suspeita".
# Havendo a resposta “sim” para 3 ou 4 perguntas, classifique-a como "Cúmplice",
# Se responder “sim” a 5 perguntas, classifique-a como "Culpada".
# Caso contrário (1 ou 0 “sim”), classifique como "Inocente".


perguntas = ['Telefonou para a vítima ?', 'Esteve no local do crime ?', 'Mora perto da vítima ?', 'Devia para a vítima ?', 'Já trabalhou com a vítima ?']
respostas = []
print ('Para cada pergunta responda com sim ou não.\n')

for i in perguntas:
   resp  = input(i)
   respostas.append(resp)

quantidade = respostas.count('sim') 
if (quantidade == 2):
   print ('Suspeita')
elif (quantidade == 3 or quantidade == 4):
   print ('Cúmplice')
elif (quantidade == 5):
   print ('Culpada')
else:
   print ('Inocente')