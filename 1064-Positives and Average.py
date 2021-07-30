a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
soma = 0
numbs = 0
x = [a, b, c, d, e, f]
for i in x:
    if float(i) > 0:
        numbs = numbs + i
        soma = soma + 1
print('{} valores positivos'.format(soma))
print('{:.1f}'.format(numbs/soma))