# 3. 14. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o caro custa R$ 60 por dia e R$ 0,15 por km rodado
km = float(input("informe a quilometragem percorrida: "))
dias = int(input("iforme a quantidade de diárias: "))

total = 60 * dias + 0.15 * km
print(f'Total a pagar: R$ {total:.2f}')