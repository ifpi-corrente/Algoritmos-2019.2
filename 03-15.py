# 3. 15. Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte  a quantidade de cigarros fumados por dia e quantos anos ele ja fumou. Considere um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
cigarros_dia = int(input("Quantos cigarros fumados por dia? "))
ano_fumante = int(input("Quantos anos você fumou? "))

restante = int((10 * cigarros_dia * 365 * ano_fumante)/(60*24))
print(f'Perdeu {restante} dias')