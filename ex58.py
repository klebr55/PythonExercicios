# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador
# vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from time import sleep
from random import randint
print(f"{'-=' * 15} "
      f"\nJogo da Advinhação V2.0 "
      f"\n{'-=' * 15}")
input("\n\nVamos jogar o jogo da advinhação!"
      "\n\nO Computador vai pensar em um número de 1 a 10 "
      "e você vai ser desafiado a advinhar em qual número ele pensou, ok?"
      "\n\nTecle 'Enter'"
      " para iniciar ")
print("\nUm momento, o computador está pensando...")
sleep(4)
print("Ok...")
sleep(0.5)
contador = 0
pc = randint(1, 10)
jogador = int(input("Tente advinhar qual número"
                    " de 1 a 10 o computador pensou: "))
while jogador != pc:
    if jogador < pc:
        contador += 1
        jogador = int(input("Mais... Tente mais uma vez"
                            "\nQual é o seu palpite?: "))
    elif jogador > pc:
        contador += 1
        jogador = int(input("Menos... Tente mais uma vez"
                            "\nQual é o seu palpite?: "))
if contador >= 1:
    print(f"Você acertou com {contador} tentativas. Parabéns!")
else:
    print("Parabéns! Acertou de primeira :)")