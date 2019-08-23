  #17 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
#O resultado do atleta será determinado pela média dos cinco valores restantes. 
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo 
#atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
#O programa deve ser encerrado quando não for informado o nome do atleta. 
#A saída do programa deve ser conforme o exemplo abaixo:
nome = 'ifpi'
atletas=[]
saltos=[]
resultados=[]

while len(nome) != 0 :
    nome=(input("Digite o nome do atleta: "))
    if len(nome) > 0:
        atletas.append(nome)
        soma = 0
        media = 0
        for i in range (5):
            distancia = float(input('Digite o salto: '))
            saltos.append(distancia)
            soma = soma + distancia
        media = soma/5
        resultados.append(media)       
print(atletas)
print(saltos)
print(resultados)
            
    				
    