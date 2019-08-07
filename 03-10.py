salario = float(input("Digite seu salário: "))
aumento = float(input("Digite o aumento em porcentagem: "))
aumento_em_reais = (salario * aumento / 100)
total = salario + aumento_em_reais
print(f'Seu salário é R$ {salario:.2f} e com o aumento de {aumento:.2f}% que representa R$ {aumento_em_reais:.2f} ficou R$ {total:.2f}')
