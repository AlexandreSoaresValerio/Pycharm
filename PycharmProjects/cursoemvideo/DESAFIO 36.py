c = float(input('Qual o valor da casa?'))
s = float(input('Qual o valor do seu salário?'))
m = float(input('Em quantos meses deseja pagar?'))
p = (c/m)+0.83/100*c
if 30/100*s > p:
    print('O valor da sua parcela será : \033[32mR${:.2f}'.format(p))
else:
    print('\033[31mSeu empréstimo foi negado!Devido ultrapassar os 30% sobre cada parcela.')