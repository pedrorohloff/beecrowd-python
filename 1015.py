import math

linha1 = str(input()).split(' ')
linha2 = str(input()).split(' ')
n1 = [float(i) for i in linha1]
n2 = [float(i) for i in linha2]

dist = math.sqrt(pow(n2[0] - n1[0], 2) + pow(n2[1] - n1[1], 2))

print(f'{dist:.4f}')
