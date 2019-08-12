valor = int(input("Digite o valor que quer sacar: "))
if (valor < 10 or valor > 600):
    print("Valor incorreto.")
else:
    notas100 = valor // 100
    notas50 = ((valor - notas100 * 100)) // 50
    notas10 = (valor - notas100 * 100 - notas50 * 50) // 10
    notas5 = (valor - notas100 * 100 - notas50 * 50 - notas10 * 10) // 5
    notas1 = (valor - notas100 * 100 - notas50 * 50 - notas10 * 10 - notas5 * 5)
    
    print(f'{notas100} notas de 100')
    print(f'{notas50} notas de 50') 
    print(f'{notas10} notas de 10') 
    print(f'{notas5} notas de 5')
    print(f'{notas1} notas de 1') 
    