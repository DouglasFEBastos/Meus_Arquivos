# Código serve para criar titulos para o mercado livre utilizando os seguintes parametros:
# Une as bases de palavra Geral e Iluminação
# Utiliza 3 palavras desse conjunto
# Máximo de 60 caracteres na string

# Printa 30 resultados aleatórios desse conjunto

import random
import itertools

def criar_string(conjunto_palavras):
  string = str(UI+" ")
  for i in range(3):
    escolhida = random.choice(conjunto_palavras)
    string += escolhida + " "
    conjunto_palavras.remove(escolhida)
  return string

geral = ['Mtb','Road','Speed','Urbano','Trilha','Estrada','Uso adulto','Ciclista','Ciclismo','Bike','Pedalar','Profissional','Esporte','Novo','Oferta','Promoção','Original','Garantia','nfe','lazer','Aerodinânimo','Varios tamanhos','Cores','conforto','Masc / Fem']
iluminação = ['led','usb','iluminação','luz','recarregável','bateria']
ajuste = ['Ajustável','Com regulagem','Com ajuste']
segurança = ['Segurança','Proteção','In mold']

UI = input()
palavras = geral
lista3 = []
lista4 = []
todas_strings = []
variaveis = list(itertools.permutations(palavras, 3))
strings_criadas = set()

while len(variaveis) > 0:
  string_palavras = criar_string(list(variaveis.pop(0)))
  if string_palavras not in strings_criadas:
    todas_strings.append(string_palavras)
    strings_criadas.add(string_palavras)

with open("listas_palavras.txt", "w") as arquivo:
  for string in todas_strings:
    if len(string) >=60:
      continue
    arquivo.write(string + "\n")
    lista3.append(string)
    
  while len(lista4)<30:

    escolhida = random.choice(lista3)
    if escolhida not in lista4:
      lista4.append(escolhida)
print('\n\n\n')

for i in range(len(lista4)):
  print(lista4[i])
