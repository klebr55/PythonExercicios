# Exercício Python 46: Faça um programa que mostre na tela uma
# contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji
print("Contagem regressiva para os fogos de artifício...")
sleep(1)
for c in range(0, 11):
    print(c)
    sleep(1)
print(emoji.emojize('EBAAAAAAAAAAAA :sparkler:'))
