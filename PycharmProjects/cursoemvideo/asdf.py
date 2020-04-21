maisVelho = 0
nomeHomemMaisVelho = ''
mulheresComMenosDeVinteAnos = 0
mediaIdade = 0
somaDasIdades = 0

for i in range(0, 4):
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade'))
    sexo = str(input('Entre c om o sexo F ou M')).upper().strip()

    if idade > maisVelho and 'M' in sexo:
        maisVelho = idade
        nomeHomemMaisVelho = nome

    if idade < 20 and 'F' in sexo:
        mulheresComMenosDeVinteAnos += 1

    somaDasIdades += idade

mediaIdade = somaDasIdades / 4

print('-='*20)

print(f'Media da idade do grupo: {mediaIdade}')
print(f'Nome do homem mais velho: {nomeHomemMaisVelho}')
print(f'Mulheres com menos de 20 anos: {mulheresComMenosDeVinteAnos}')