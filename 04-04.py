#4.4. Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
salario = float(input("Digite o salário: "))
if (salario > 1250):
    aumento = salario * 0.1
    print(f"O salário R$ {salario:.2f} teve aumento de R$ {aumento:.2f} e ficou R$ {salario + aumento:.2f}")
if (salario <= 1250):
    aumento = salario * 0.15
    print(f"O salário R$ {salario:.2f} teve aumento de R$ {aumento:.2f} e ficou R$ {salario + aumento:.2f}")