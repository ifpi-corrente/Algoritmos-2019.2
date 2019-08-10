numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
operacao = input("Digite a operação (+ - * /): ")

if (operacao == '+'):
    resultado = numero1 + numero2
elif(operacao == '-'):
    resultado = numero1 - numero2
elif(operacao == '*'):
    resultado = numero1 * numero2
elif(operacao == '/'):
    resultado = numero1 / numero2

print(f"{numero1} {operacao} {numero2} = {resultado}")