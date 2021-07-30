x = float(input())
if x >= 0 and x <= 400.00:
    print('Novo salario: %.2f'%(x*1.15))
    print('Reajuste ganho: %.2f'%(x*0.15))
    print('Em percentual: 15 %')
elif x >= 400.01 and x <= 800.00:
    print('Novo salario: %.2f'%(x*1.12))
    print('Reajuste ganho: %.2f'%(x*0.12))
    print('Em percentual: 12 %')
elif x >= 800.01 and x <= 1200.00:
    print('Novo salario: %.2f'%(x*1.10))
    print('Reajuste ganho: %.2f'%(x*0.10))
    print('Em percentual: 10 %')
elif x >= 1200.01 and x <= 2000.00:
    print('Novo salario: %.2f'%(x*1.07))
    print('Reajuste ganho: %.2f'%(x*0.07))
    print('Em percentual: 7 %')
elif x > 2000.00:
    print('Novo salario: %.2f'%(x*1.04))
    print('Reajuste ganho: %.2f'%(x*0.04))
    print('Em percentual: 4 %')