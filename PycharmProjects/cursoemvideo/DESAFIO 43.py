alt = float(input(' Qual sua altura? (m)'))
peso = float(input(' Qual seu peso? (Kg)'))
imc = peso/(alt*alt) #peso (altura**2)
print('Seu imc é {:.2f} '.format(imc), end=' ')
if imc < 18.5:
    print('Abaixo do peso normal.')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obessidade')
else:
    print('Obesidade mórbida')
