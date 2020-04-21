n = int(input('Digite um numero inteiro :'))
print('''Escolha uma das bases para conversão:
[1] conerter para binário
[2] converte para octal
[3] converter para hexadecimal''')
opção = int(input('Sua opção :'))
if opção == 1 :
    print('{} convertido para binário é {}'.format(n,bin(n)[2:]))
elif opção == 2:
    print('{} convertido para octal é {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é {}'.format(n,hex(n)[2:]))
else:
    print('Opção inválida.Tente novamente')

