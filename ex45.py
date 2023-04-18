# Exercício Python 45: Crie um programa que faça o
# computador jogar Jokenpô com você.

import random
from time import sleep
# Define as cores em variáveis
preto = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
magenta = '\033[0;35m'
alaranjado = '\033[0;36m'
branco = '\033[48;2;255;255;255m'
stopcolor = '\033[m'

# Define os estilos em variáveis
negrito = '\033[1m'
italico = '\033[3m'
sublinhado = '\033[4m'
piscante = '\033[5m'
inverso = '\033[7m'
oculto = '\033[8m'

print(f"{'-=' * 10}"
      f"\nVAMOS JOGAR JOKENPÔ"
      f"\n{'-=' * 10}")
jogador = int(input(f"\n{magenta}{'=' * 5} Suas opções {'=' * 5}{stopcolor}"
                    f"{vermelho}\n[1] Pedra {stopcolor}"
                    f"{amarelo}\n[2] Papel {stopcolor}"
                    f"{verde}\n[3] Tesoura {stopcolor}"
                    f"{negrito}\n\nSua escolha: {stopcolor}"))
if jogador == 1:
    jogador = f"{vermelho}pedra{stopcolor}"
elif jogador == 2:
    jogador = f"{amarelo}papel{stopcolor}"
elif jogador == 3:
    jogador = f"{verde}tesoura{stopcolor}"

pc = random.randint(1, 3)
if pc == 1:
    pc = f"{vermelho}pedra{stopcolor}"
elif pc == 2:
    pc = f"{amarelo}papel{stopcolor}"
elif pc == 3:
    pc = f"{verde}tesoura{stopcolor}"

print(f"\nOk, lá vai...")
sleep(3)
print(f"{azul}JO{stopcolor}")
sleep(1.5)
print(f"{amarelo}KEN{stopcolor}")
sleep(1.5)
print(f"{vermelho}PÔ!{stopcolor}")
sleep(0.5)

print(f"\n{negrito}Você jogou {jogador} {negrito}e o computador jogou {pc}{stopcolor}")
if jogador == f"{vermelho}pedra{stopcolor}" and pc == f"{verde}tesoura{stopcolor}":
    print(f"{verde + negrito}Parabéns! Você venceu{stopcolor}")
elif jogador == f"{amarelo}papel{stopcolor}" and pc == f"{vermelho}pedra{stopcolor}":
    print(f"{verde + negrito}Parabéns! Você venceu{stopcolor}")
elif jogador == f"{verde}tesoura{stopcolor}" and pc == f"{amarelo}papel{stopcolor}":
    print(f"{verde + negrito}Parabéns! Você venceu{stopcolor}")
elif jogador == pc:
    print(f"{amarelo + negrito}Empate!{stopcolor}")
else:
    print(f"{vermelho + negrito}Você perdeu{stopcolor}")