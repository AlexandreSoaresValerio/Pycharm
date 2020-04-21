frase = str(input('Digite uma frase:'.strip().upper()))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print('O inverso de {} é {} \nTemos um palindromo. '.format(frase, inverso))
else:
    print('O inverso de {} é {} \nA frase não é um palindromo.'.format(frase, inverso))


