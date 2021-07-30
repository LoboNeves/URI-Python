soma = 0
qtd = 0
while qtd < 2:
    a = float(input())
    if a >= 0 and a <= 10:
        soma = soma + a
        qtd = qtd +1
    else:
        print('nota invalida')
print('media = %.2f' % float(soma/qtd))