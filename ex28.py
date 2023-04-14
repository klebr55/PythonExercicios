# Exercício Python 28: Escreva um programa que faça o computador
# “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa
# deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print(f"{'=' * 17} Jogo da advinhação V1.0 {'=' * 17}")
input("\nAperte enter para iniciar!")
print(f"\n{'=' * 33}"
      "\nUm momento, o PC está pensando..."
      f"\n{'=' * 33}")
sleep(5)
print("\nOk, tudo certo :)")
sleep(0.5)
pc = random.randrange(0, 5)
usuario = int(input("\nTente adivinhar em qual número de 0 a 5 o computador pensou: "))
if usuario == pc:
    print("\nResultado: Você acertou! Parabéns")
else:
    print(f"\nResultado: Você errou, o valor sorteado foi {pc}")