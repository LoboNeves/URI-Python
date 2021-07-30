lista = []
maior = 0
posicao = 0
n = 0
while n < 100:
    x = int(input())
    lista.append(x)
    n += 1
    if x > maior:
        maior = x
        posicao = lista.index(x) + 1
print(maior)
print(posicao)