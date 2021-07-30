N = int(input())
qtd = 0
while qtd < N:
    x = input().split()
    qtd += 1
    a = float(x[0])
    b = float(x[1])
    c = float(x[2])
    print('%.1f' % float((a*2 + b*3 + c*5)/(2 + 3 + 5)))