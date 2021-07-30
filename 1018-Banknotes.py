x = int(input())
if x>0 and x<1000000:
    print(x)
n100 = x//100
n50 = x%100//50
n20 = x%100%50//20
n10 = x%100%50%20//10
n5 = x%100%50%20%10//5
n2 = x%100%50%20%10%5//2
n1 = x%100%50%20%10%5%2
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))