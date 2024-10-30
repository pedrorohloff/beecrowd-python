a = input()
b = input()
c = input()

if float(a) <= 10 and float(b) <= 10 and float(c) <= 10:
    if float(a) >= 0 and float(b) >= 0 and float(c) >= 0:
        prod = (float(a) * 2 + float(b) * 3 + float(c) * 5) / 10

print(f'MEDIA = {prod:.1f}')