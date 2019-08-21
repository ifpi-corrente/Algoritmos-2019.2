#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
#Imprima os três vetores.

numeros=[]
pares=[]
impares=[]
for i in range(20):
  numeros.append(int(input('Digite um numero: ')))

for i in numeros:
  if i %2==0:
    pares.append(i)
  else: 
    impares.append(i)
print(pares)
print(impares)
print(numeros)

