a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
pares = 0
impares = 0
positivos = 0
negativos = 0
vals = (a, b, c, d, e)
for i in vals:
    if i % 2 == 0:
        pares += 1
    if i % 2 != 0:
        impares += 1
    if i > 0:
        positivos += 1
    if i < 0:
        negativos += 1
print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivos))
print('{} valor(es) negativo(s)'.format(negativos))