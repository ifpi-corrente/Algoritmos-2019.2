## 3.12. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input("Digite a distância em Km: "))
velocidade = float(input("Digite a velocidade em Km/h: "))

tempo_em_minutos = (distancia / velocidade) * 60
horas = int(tempo_em_minutos // 60)
minutos = int(tempo_em_minutos % 60)
segundos = int((tempo_em_minutos % 1) * 60 )
print(f"O tempo estimado da viagem é {horas} horas e {minutos} minutos e {segundos} segundos")