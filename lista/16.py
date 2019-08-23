#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
vendedores = int(input("Digite a quantidade de vendedores: "))
salarios = [0,0,0,0,0,0,0,0,0]

for i in range(vendedores):
    bruta = float(input("Qual o valor da sua venda bruta ? "))
    comissao = bruta * 9 / 100
    total =  comissao + 200
    if total <= 299 :
        salarios[0] = salarios[0] + 1
    elif total <= 399:
         salarios[1] = salarios[1] + 1
    elif total <= 499:
        salarios[2] = salarios[2] + 1
    elif total <= 599:
        salarios[3] = salarios[3] + 1
    elif total <= 699:
        salarios[4] = salarios[4] + 1
    elif total <= 799:
        salarios[5] = salarios[5] + 1
    elif total <= 899:
        salarios[6] = salarios[6] + 1
    elif total <= 999:
        salarios[7] = salarios[7] + 1
    else:
        salarios[8] = salarios[8] + 1
        
print(salarios)