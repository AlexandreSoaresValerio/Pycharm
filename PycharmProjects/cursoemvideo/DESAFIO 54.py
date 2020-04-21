from datetime import date
maior = 0
menor = 0
for c in range(1, 7):
    i = int(input('Qual sua data de nascimento da {}º pessoa?'.format(c)))
    if date.today().year - i >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} pessoas já atingiram a maioridade.'.format(maior))
print('{} pessoas ainda não atingiram a maioridade .'.format(menor))


