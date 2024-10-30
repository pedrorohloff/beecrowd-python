nome = input()
sal_fixo = input()
vendas = input()
sal_total = float(sal_fixo) + float(vendas) * 0.15
print(f'TOTAL = R$ {sal_total:.2f}')