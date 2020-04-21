n1 = float(input('Primeiro segmento:'))
n2 = float(input('Segundo segmento:'))
n3 = float(input('Terceiro segmento:'))
if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1 + n2:
    print('\33[1;32mOs segmentos acima podem formar um triangulo')
else:
    print('\33[1;32mOs segmentos acima não podem formar um triangulo')