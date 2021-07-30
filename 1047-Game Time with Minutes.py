n = input().split()
ih = int(n[0])
im = int(n[1])
fh = int(n[2])
fm = int(n[3])
if ih == fh == im == fm:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif fh >= ih and fm >= im:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(fh - ih, fm - im))
elif fh >= ih and im > fm:
    if fh - ih == 1:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(0, 60 - (im - fm)))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(fh - ih, 60 - (im - fm)))
elif ih > fh and fm >= im:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 - (ih - fh), fm - im))
elif ih > fh and im > fm:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24 - (ih - fh) - 1, 60 - (im - fm)))