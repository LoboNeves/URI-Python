x = []
soma = 0
soma2 = 0
N = int(input())
for i in range(1, N + 1):
    x.append(int(input()))
for i in x:
    if 10 <= i <= 20:
        soma += 1
    elif i < 10 or i > 20:
        soma2 += 1
print('%d in' % soma)
print('%d out' % soma2)