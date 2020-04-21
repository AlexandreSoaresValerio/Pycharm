velho = ''
soma = 0
somaidade = 0
maior = 0
for c in range(1, 3):
    print('-'*3, '{}º Pessoa'.format(c), '-'*3)
    n = str(input('Nome:')).strip()
    i = float(input('Idade:'))
    s = str(input('Sexo [M/F]'))
    somaidade += i
    if i > maior and s in 'Mm':
        maior = i
        velho = n
    if s in 'Ff' and i < 20:
        soma += 1
media = somaidade/4
print('O homem mais velho do grupo é {}'.format(velho))
print('A idade média do grupo é {:.0f} anos'.format(somaidade))
print('Tem {} mulheres com menos de 20 anos.'.format(soma))





