# Exercício Python 45: Crie um programa que faça o
# computador jogar Jokenpô com você.

import random
print("VAMOS JOGAR JOKENPÔ")
jogador = int(input("Suas opções: "
                    "\n[1] Pedra"
                    "\n[2] Papel"
                    "\n[3] Tesoura"
                    "\nSua escolha: "))
if jogador == 1:
    jogador = "pedra"
elif jogador == 2:
    jogador = "papel"
elif jogador == 3:
    jogador = "tesoura"

pc = random.randint(1, 3)
if pc == 1:
    pc = "pedra"
elif pc == 2:
    pc = "papel"
elif pc == 3:
    pc = "tesoura"

print(f"Você jogou {jogador} e o computador jogou {pc}")
