vals = input().split()
a = int(vals[0])
b = int(vals[1])
c = int(vals[2])
if a < b and a < c:
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
if b < a and b < c:
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
if c < a and c < b:
    print(c)
    if a < b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
print()
print(a)
print(b)
print(c)