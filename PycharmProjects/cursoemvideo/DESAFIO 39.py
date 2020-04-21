from datetime import date
s = str(input('Qual o sexo?'))
if s == 'masculino':
    print('Bem vindo a calculadora de alistamento militar')
    a = int(input('Ano de nascimento:'))
    print('Quem nasceu em {} tem {} anos em {}'.format(a, date.today().year - a, date.today().year))
    d = 18
    if date.today().year - a < 18:
        print('Ainda faltam {} anos para o alistamento'.format(d - (date.today().year - a)))
        print('Seu alistamento será em {}'.format(d - (date.today().year - a) + date.today().year))
    elif date.today().year - a > 18:
        print('Você já deveria ter se alistado há {} anos'.format(date.today().year - a - d))
        print('Seu alistamento foi em {}'.format(date.today().year - (date.today().year - a - d)))
    elif date.today().year - a == 18:
        print('Você tem que se alistar imediatamente!')
else:
    print('Você não precisa se alistar')
