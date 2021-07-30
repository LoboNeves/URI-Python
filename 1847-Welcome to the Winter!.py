temps = input().split()
a = int(temps[0])
b = int(temps[1])
c = int(temps[2])
if a > b and c >= b:
    print(':)')
elif b > a and b >= c:
    print(':(')
elif b > a and c > b and (c - b) < (b - a):
    print(':(')
elif b > a and c > b and (c - b) >= (b - a):
    print(':)')
elif a > b and b > c and (b - c) < (a - b):
    print(':)')
elif a > b and b > c and (b - c) >= (a - b):
    print(':(')
elif a == b and c > b:
    print(':)')
elif a == b and b > c:
    print(':(')
else:
    print(':(')