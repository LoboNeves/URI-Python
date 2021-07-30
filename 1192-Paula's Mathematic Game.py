N = int(input())
for i in range(N):
    s = input()
    a = int(s[0])
    b = (s[1])
    c = int(s[2])
    if c == a:
        print(c*a)
    elif b.islower():
        print(c + a)
    elif b.isupper():
        print(c - a)