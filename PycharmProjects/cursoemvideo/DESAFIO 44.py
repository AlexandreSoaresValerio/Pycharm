p = float(input('Qual o preço do produto?'))
print('''Escolha qual a forma de pagamento :
[1] À vista no dinheiro com desconto de 10%
[2] À vista no cartão de debito com desconto de 5%
[3] Em até 2x no cartão preço normal
[4] 3x mais com 20% de juros sobre o preço normal do produto''')
c = float(input('Escolha uma condição de pagamento :'))
if c == 1:
    print('O preço do produto é R$\033[34m{:.2F}\033[m e com o desconto ficará R$\033[34m{:.2F}\033[m'.format(p, p - (10/100*p)))
elif c == 2:
    print('O preço do produto é R$\033[32m{:.2F}\033[m e com o desconto ficará R$\033[32m {:.2F}\033[m'.format(p, p - (5/100*p)))
elif c == 3:
    print('Preço normal em 1x é de R$\033[33m{:.2F}\033[m ou 2x de R$\033[33m{:.2F}\033[m'.format(p, p/2))
if c == 4:
    x = int(input('Escolha em quantas vezes deseja fazer o pagamento :'))
    print('Preço total com juros ficará R$\033[33m{:.2F}\033[m e parcelado em \033[36m{:.0f}\033[mx de R$\033[33m{:.2F}\033[m por mês.'.format(p+(20/100*p), x, (p + (20/100*p))/x))

