#Foram anotadas as idades e alturas de 30 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura 
#inferior à média de altura desses alunos.
idade = []
alt = []
quant = 0
soma = 0
for i in range (5):
  idade.append(int(input('Digite sua idade:  ')))
  alt.append(int(input('Digite sua altura:  ')))
  soma = soma + alt[i]
media = soma/len (alt)
for j in range (5):
  if idade[j] > 13 and alt[j] < media:
    quant= quant + 1
    
print(quant)