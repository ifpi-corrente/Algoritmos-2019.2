# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80km/h.
velocidade = float(input("Digite a velocidade em Km/h: "))

if velocidade > 80:
    print("Você foi multado !!")
    valor = (velocidade - 80) * 5
    print(f"Sua multa é de R$ {valor}")