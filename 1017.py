tempo_gasto = int(input())
vel_med = int(input())
km_litro = 12

qtd_litro = (tempo_gasto * vel_med) / km_litro

print(f'{qtd_litro:.3f}')