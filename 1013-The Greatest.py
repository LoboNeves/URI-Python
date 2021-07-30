valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
calculo = (a + b + abs(a - b))/2
calculo2 = (calculo + c + abs(calculo - c))/2
print('{} eh o maior'.format(int(calculo2)))