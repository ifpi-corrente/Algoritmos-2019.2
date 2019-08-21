#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

numero1 = []
numero2 = []
numero3 = []
numero4 = []
for i in range(10):
  numero1.append(int(input('Digite um número para primeiro vetor: ')))

print(numero1)
  
for i in range(10):
  numero2.append(int(input('Digite um número para segundo vetor: ')))

print(numero2)
for i in range(10):
  numero3.append(int(input('Digite um número para terceiro vetor: ')))
  
print(numero3)
  
for j in range(10):
  numero4.append(numero1[j])
  numero4.append(numero2[j])
  numero4.append(numero3[j])
print(numero4)