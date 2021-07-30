x = []
N = int(input())
for i in range(1, N + 1):
    x.append(int(input()))
for i in x:
    if i > 0 and i % 2 == 0:
        print('EVEN POSITIVE')
    elif i > 0 and i % 2 != 0:
        print('ODD POSITIVE')
    elif i < 0 and i % 2 == 0:
        print('EVEN NEGATIVE')
    elif i < 0 and i % 2 != 0:
        print('ODD NEGATIVE')
    elif i == 0:
        print('NULL')