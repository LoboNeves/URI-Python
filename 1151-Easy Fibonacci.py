n = int(input())
a = 0
b = 1
print('{} {}'.format(a, b), end='')
for i in range(n - 2):
    c = a + b
    print(' {}'.format(c), end='')
    a = b
    b = c
print()