linha1 = input()
linha2 = input()

linha1 = linha1.split(' ')
linha2 = linha2.split(' ')

qtd1 = linha1[1]
preco1 = linha1[2]
qtd2 = linha2[1]
preco2 = linha2[2]

total = float(qtd1) * float(preco1) + float(qtd2) * float(preco2)

print(f'VALOR A PAGAR: R$ {total:.2f}')