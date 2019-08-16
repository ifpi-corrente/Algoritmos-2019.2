segundos = int(input())

##Calcular a quantidade de horas
horas = segundos // 3600

##Calcular a quantidade de minutos
temporestante = segundos - (horas * 3600)
minutos = temporestante // 60 

##Calcular a quantidade de segundos
segundos = temporestante % 60

print('{}:{}:{}'.format(horas,minutos,segundos))