numbs = input().split()
x = int(numbs[0])
y = int(numbs[1])
z = 0
lista = ''
while z < y:
    z = z + 1
    lista = lista + str(z) + ' '
    if z % x == 0:
        lista=lista[0:len(lista)-1]
        print(lista)
        lista = ''
    elif z == y:
        lista = lista[0:len(lista) - 1]
        print(lista)