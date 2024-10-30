linha = (input().split(' '))

a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

maxAB = (a + b + abs(a - b)) / 2
max_total = (maxAB + c + abs(maxAB - c)) / 2


print(f'{max_total:.0f} eh o maior')