n = int(input('Digite um numero :'))
count = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end='')
        count = count+1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end=' ')
print('\n \033[mo numero {} pode ser dividido {} vezes'.format(n, count))
if count == 2:
    print(' o numero {} é primo'.format(n))
else:
    print(' o numero {} não é primo'.format(n))

