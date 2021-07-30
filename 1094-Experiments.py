n = int(input())
somaT = 0
somaC = 0
somaR = 0
somaS = 0
for i in range(n):
    x = input().split()
    somaT += int(x[0])
    if x[1] == 'C':
        somaC += int(x[0])
    elif x[1] == 'R':
        somaR += int(x[0])
    elif x[1] == 'S':
        somaS += int(x[0])
print('Total: {} cobaias'.format(somaT))
print('Total de coelhos: {}'.format(somaC))
print('Total de ratos: {}'.format(somaR))
print('Total de sapos: {}'.format(somaS))
print('Percentual de coelhos: {:.2f} %'.format(float(somaC * (100/somaT))))
print('Percentual de ratos: {:.2f} %'.format(float(somaR * (100/somaT))))
print('Percentual de sapos: {:.2f} %'.format(float(somaS * (100/somaT))))