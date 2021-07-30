x = int(input())
anos = x//365
meses = x % 365//30
dias = x % 365 % 30
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))