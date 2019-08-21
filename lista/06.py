#Faça um Programa que peça as quatro notas de 10 alunos, 
#calcule e armazene num vetor a média de cada aluno, 
#imprima o número de alunos com média maior ou igual a 7.0.
notas =[]
medias = []
for i in range(4):
    notasAluno = []
    soma = 0 
    for j in range(4):
        notasAluno.append(float(input(f"Digite a {j+1} nota do aluno {i+1}: ")))
        soma = soma + notasAluno[j]
    media = soma/4
    medias.append(media)
print(medias)

cont = 0
for i in medias:
    if i>= 7.0:
        cont+=1
print(f'{cont} alunos tiraram 7 ou mais.')
        
