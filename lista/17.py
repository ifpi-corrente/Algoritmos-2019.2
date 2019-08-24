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
ordem = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']

while len(nome) != 0 :
    nome=(input("Digite o nome do atleta: "))
    if len(nome) > 0:
        atletas.append(nome)
        soma = 0
        media = 0
        for i in range (5):
            distancia = float(input(f'{ordem[i]} salto: '))
            saltos.append(distancia)
            soma = soma + distancia
        media = soma/5
        resultados.append(media)       

vezes = len(atletas)

x = 0
for i in range(vezes):
    
    print(f'Atleta: {atletas[i]}')
    print(f'Saltos: ',end="")
    for j in range(5):
        print(f'{saltos[x]} - ', end="")
        x = x + 1
    print("")
    print(f'Média dos saltos: {resultados[i]}m')
    
    

#print(atletas)
#print(saltos)
#print(resultados)
            
    				
    