#Faça um programa que receba a temperatura média de cada mês do ano e 
#armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e 
#mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram 
#(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas = []
soma = 0
for i in range (12):
  temperaturas.append(float(input(f"Digite a temperatura do mês {i + 1}: ")))
  soma = soma + temperaturas[i]
media = soma/len(temperaturas)
for j in temperaturas:
  if j > media:
    print(j)
 
  