n1 = float(input('Primeira nota :'))
n2 = float(input('Segunda nota:'))
media = (n1+n2)/2
print('Tirando {} e {},a média do aluno será {}'.format(n1, n2, media))
if media > 7:
    print('O aluno está aprovado.')
elif media >= 5 < 7:
    print('O aluno está de recuperação.')
else:
    print('O aluno está reprovado.')
