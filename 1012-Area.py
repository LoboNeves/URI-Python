A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
areaTri = (A*C)/2
areaO = pi*C**2
areaTra = (B+A)*C/2
areaSqu = B**2
areaRec = A*B
print('TRIANGULO: %.3f'%areaTri)
print('CIRCULO: %.3f'%areaO)
print('TRAPEZIO: %.3f'%areaTra)
print('QUADRADO: %.3f'%areaSqu)
print('RETANGULO: %.3f'%areaRec)