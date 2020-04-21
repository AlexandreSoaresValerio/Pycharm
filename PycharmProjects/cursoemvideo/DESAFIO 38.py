p = int(input('Primeiro número:'))
s = int(input('Segundo número:'))
if p>s:
    print('\033[35mO primeiro valor é maior')
elif s>p:
    print('\033[32mO segundo valor é maior')
elif p==s:
    print('\033[34mOs dois valores são iguais')