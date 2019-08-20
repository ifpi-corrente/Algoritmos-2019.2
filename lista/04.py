 #Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
caracteres = []
consoantes = []
vogais = ["a", "e", "i", "o", "u"]
for i in range(10):
  caracteres.append(input("Digite um caractere: "))
  if not(caracteres[i] in vogais):
    consoantes.append(caracteres[i])
print(len(consoantes))
print(consoantes)