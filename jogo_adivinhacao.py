from random import random
print("Bem vindo ao jogo de adivinhação!!")

jogador = input("Digite seu nome, jogador: ")
print(f'Vamos começar o jogo {jogador} ...')
chute = input("Digite um número ente 0 e 100 ")
valor = int(random() * 100)
chute = int(chute)
if (chute == valor):
    print('Acertou')
else:
    print(f'Errou pq a resposta certa {valor}')
