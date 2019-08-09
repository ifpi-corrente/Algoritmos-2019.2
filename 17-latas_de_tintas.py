metros2 = float(input("Digite a metargem da area pintada: ")) * 1.1
litros = metros2 / 6
latas = int(litros / 18)
if (litros % 18 != 0):
    latas += 1
print("----- Situação 1 -----")
print(f'Será necessário {latas} latas')
gastar = latas * 80
print(f'Total R$ {gastar}')

print("----- Situação 2 -----")
galoes = int(litros/3.6)
if (litros % 3.6 != 0):
    galoes +=1
print(f'Será necessário {galoes} galoes')
print(f'Total R$ {galoes * 25}')

print("----- Situação 3 -----")
mixlatas = int(litros/ 18)
mixgaloes = int((litros - (mixlatas * 18))/3.6)
if (litros - (mixlatas * 18) % 3.6 != 0):
    mixgaloes += 1
print(f'{mixlatas} latas e {mixgaloes} galões')
print(f'Total R$ {mixlatas * 80 + mixgaloes* 25}')
