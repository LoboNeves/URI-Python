a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
soma = 0
for i in [a, b, c, d, e]:
    if i % 2 == 0:
        soma = soma + 1
print('{} valores pares'.format(soma))