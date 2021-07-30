N = int(input())
contador = 0
soma = 0
while contador < N:
    soma = 0
    x = int(input())
    contador += 1
    for i in range(1, x):
        if x % i == 0:
            soma += i
    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))