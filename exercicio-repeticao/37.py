#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigo = 1
alto = None
baixo = None
magro = None
gordo = None
totalpeso = 0
totalaltura = 0
cont = 0

while codigo != 0 :
    codigo = int(input("Digite o código: "))
    if codigo == 0:
        break
    altura = float(input("Digite a altura em cm: "))
    totalaltura = totalaltura + altura
    if alto == None:
        alto = altura
        baixo = altura
    if altura > alto:
        alto = altura
    if altura < baixo:
        baixo = altura
        
    peso = float(input("Digite o peso em Kg: "))
    totalpeso = totalpeso + peso
    if magro == None:
        magro = peso
        gordo = peso
    
    if peso > gordo:
        gordo = peso
    if peso < magro:
        magro = peso
    cont = cont + 1

#+alto, +baixo, +gordo, +magro, media altura, media peso
print(f'O mais é alto{alto}, o mais baixo é {baixo}')
print(f'O mais gordo é {gordo} e o mais magro é {magro}')
print(f'A média da altura é {totalaltura/cont}')
print(f'A média da peso é {totalpeso/cont}')