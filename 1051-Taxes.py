x = float(input())
if x <= 2000.00:
    print('Isento')
elif 2000.00 < x <= 3000.00:
    print('R$ %.2f' % ((x - 2000.00) * 0.08))
elif 3000.00 < x <= 4500.00:
    print('R$ %.2f' % ((1000.00 * 0.08) + ((x - 3000.00) * 0.18)))
elif x > 4500.00:
    print('R$ %.2f' % ((1000.00 * 0.08) + (1500.00 * 0.18) + ((x - 4500.00) * 0.28)))