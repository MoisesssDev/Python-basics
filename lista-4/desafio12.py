# Crie uma lista com 10 caracteres (letras). Faça um programa que leia a lista e diga quantas consoantes
# existem na lista. Depois, utilize uma string (ao invés de uma lista) e faça um programa para fazer o mesmo.

letras = ['a', 'b', 'z', 'h', 'o', 'l', 'j', 'h', 'o', 'l']

qtd = 0
for i in letras:
   if (i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != ''):
      qtd = qtd +1
      
print ('Quantidade de consoantes na lista',letras, 'é', qtd) 

palavra = 'saulomatos'

qtd = 0
for i in palavra:
   if (i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u'):
      qtd = qtd +1

print ('Quantidade de consoantes na string',palavra, 'é', qtd)