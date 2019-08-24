#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
resposta = 1
resultado = [0,0,0,0,0,0]
soma = 0
SO =['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
while resposta != 0 :
    print("Qual o melhor Sistema Operacional para uso em servidores?")
  
    print("As possíveis respostas são : ")
    print("1- Windows Server")
    print("2- Unix")
    print("3- Linux")
    print("4- Netware")
    print("5- Mac OS")
    print("6- Outro")
        
    resposta = int(input("Qual é a resposta? "))
    if resposta >0 and resposta < 7:
        resultado[resposta-1] = resultado[resposta-1] + 1 
        soma += 1
        
        
print(resultado)
for i in range(6):
        print(f'{SO[i]} {resultado[i]} {resultado[i]*100/soma:.0f}%')
    
print('total:',soma)


maior = 0 
indice = 0
for i in range(6):
    if resultado[i] > maior :
        maior = resultado[i]
        indice = i
    

print(f'O mais votado é o {SO[indice]} que teve {maior} votos')
