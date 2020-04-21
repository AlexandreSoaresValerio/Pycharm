import emoji
from time import sleep
print('Começando a contagem regressiva para queima de fogos')
sleep(2)
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize('BOOOM :boom:', use_aliases=True))
