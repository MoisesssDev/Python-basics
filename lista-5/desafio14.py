# Crie um dicionário vazio para armazenar 3 senhas (chave) de atendimento e o respectivo nome (valor)
# do cliente. Cada senha e cada nome serão digitados pelo usuário. Para as senhas utilize um número inteiro
# positivo com 2 dígitos e para o nome utilize string. Utilize a estrutura de repetição while para forçar que
# cada senha digitada seja maior ou igual a 10 e menor que 100, ou seja: “10 <= senha < 100” .
# Por fim, imprima o nome do cliente utilizando o get(), passando como parâmetro uma das três senhas.
# Ou seja: “print (dicionario.get(alguma_senha))”

atendimento = {}
for i in range(3):
   nome = input ('Informe o nome do cliente : ')
   
   while (True):         
      senha = eval(input('Informe a senha :  '))   
      if (10 <= senha < 100): 
         break
      
   atendimento[senha] = nome

consulta = eval (input('Digite uma das senhas cadastradas : '))

print ("Cliente =", atendimento.get(consulta))