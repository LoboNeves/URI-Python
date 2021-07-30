N = int(input())
vezes = 0
while vezes < N:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if y == 0:
        print('divisao impossivel')
    else:
        print(x/y)
    vezes += 1