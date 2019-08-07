## 3.11. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor de desconto e o preço a pagar.

preco = float(input("Digite o valor da mercadoria: "))
desconto = float(input("Digite o percentual do desconto: "))

desconto_em_reais = (preco * desconto/ 100)
print(f'O desconto é: R$ {desconto_em_reais}')
print(f'O valor final é R$ {preco-desconto_em_reais}')
