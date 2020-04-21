p = int(input('Qual o primeiro termo da PA?'))
r = int(input('Qual a razão da PA?'))
t = p+(10-1)*r
for c in range(p, t+r, r):
    print('{}'.format(c), end='- ')
print('Fim')
