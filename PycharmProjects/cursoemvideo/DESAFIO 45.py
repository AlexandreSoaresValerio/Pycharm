from random import randint,choice
from time import sleep
print('Bem vindo ao jogo de jokenpô')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
opção = int(input('Qual a sua jogada?'))
sleep(0)
print('JO')
sleep(0)
print('KEN')
sleep(0)
print('PÔ!!!')
itens = ('Pedra', 'Papel', 'Tesoura')
print('O computador jogou {}'.format(randint(itens)))
if opção == 0:
    print('O jogador jogou Pedra')
elif opção == 1:
    print('O jogador jogou Papel')
elif opção == 2:
    print('O jogador jogou Tesoura')
if itens == 'Pedra' and opção == 0:
    print('Empate')
    elif itens == 'Papel' and opção == 1:
    print('O JOGADOR VENCEU!')
    elif itens == 'Tesoura' and opção == 2:
    print('O computador venceu')
elif itens == 'Papel' and opção == 0:
    print('O computador venceu')
    elif itens == 'Papel' and opção == 1:
    print('EMPATE TENTE NOVAMENTE')
    elif itens == 'Papel' and opção == 2:
    print('O JOGADOR VENCEU')
elif itens == 'Tesoura' and opção == 0:
    print('O JOGADOR VENCEU')
    elif itens == 'Tesoura' and opção == 1:
    print('O COMPUTADOR VENCEU')
    elif itens == 'Tesoura' and opção == 2:
    print('EMPATE')










