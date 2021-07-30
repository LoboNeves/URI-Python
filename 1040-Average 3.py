n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
m = (n1*2 + n2*3 + n3*4 + n4*1)/10
print('Media: %.1f' %m)
if m >= 7.0:
    print('Aluno aprovado.')
elif m < 5.0:
    print('Aluno reprovado.')
elif 5.0 <= m <= 6.9:
    print('Aluno em exame.')
    ne = float(input())
    print('Nota do exame: %.1f' %ne)
    nm = (ne + m)/2
    if nm >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' %nm)
    elif nm <= 4.9:
        print('Aluno reprovado')
        print('Media final: %.1f' %nm)