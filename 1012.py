linha1 = input()
linha1 = linha1.split(' ')
a = float(linha1[0])
b = float(linha1[1])
c = float(linha1[2])
PI = 3.14159

triangulo = (a * c) / 2
circulo = PI * pow(c, 2)
trapezio = ((a + b) * c) / 2
quadrado = pow(b, 2)
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')
