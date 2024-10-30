n = float(input())

taxa = 1
imposto = 0
valor = 0
temp = 0

while n > 2000.00:
    if n > 4500.00:
        taxa = 28
        temp = n % 4500
        valor = (n * temp) / 100
        n -= temp
    elif n > 3000.00:
        taxa = 18
        temp = n % 3000
        valor = (n * temp) / 100
        n -= temp
    elif n > 2000.00:
        taxa = 8
        temp = n % 2000
        valor = (n * temp) / 100
        n -= temp
    imposto += valor


print(imposto) # nao completo