x, y = input().split()
x = int(x)
y = int(y)
if x == 1:
    print('Total: R$ %.2f'%(4*y))
elif x == 2:
    print('Total: R$ %.2f'%(4.50*y))
elif x == 3:
    print('Total: R$ %.2f'%(5*y))
elif x == 4:
    print('Total: R$ %.2f'%(2*y))
elif x == 5:
    print('Total: R$ %.2f'%(1.50*y))