from datetime import date
n1 = int(input('Qual seu ano de nascimento?'))
ano = date.today().year
idade = ano - n1
print('O atleta tem {}'.format(idade))
if idade <= 9:
    print('Classificação : Mirim')
elif idade <= 14:
    print('Classificação : Infántil')
elif idade <= 19:
    print('Classificação : Junior')
elif idade <= 25:
    print('Classificação : Sênior')
elif idade > 25:
    print('Classificação : Master')