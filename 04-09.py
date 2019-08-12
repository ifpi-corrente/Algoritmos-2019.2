casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário: "))
anos = int(input("Digite os anos que quer pagar: "))

valor_max = salario * 0.3
prestacao = casa / (anos * 12)
if (prestacao <= valor_max):
    print("Compra aprovada!")
    print(f'Á prestação ficou R$ {prestacao} em {anos * 12} meses')
else:
    print("Compra não aprovada!")
    print(f'A prestação ficou {prestacao}')