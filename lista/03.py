  #Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
  notas.append(float(input(f'Digite {i+1}ª nota: ')))

soma = 0
for i in (notas):
  soma = soma + i
  print(i)
print(f'A média é {soma/len(notas)}')