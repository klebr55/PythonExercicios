# Exercício Python 52: Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
preto = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
magenta = '\033[0;35m'
alaranjado = '\033[0;36m'
branco = '\033[48;2;255;255;255m'
stopcolor = '\033[m'

tot = 0
numero = int(input("Digite um número: "))
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f"{amarelo}", end=f'{stopcolor}')
        tot += 1
    else:
        print(f"{vermelho}", end=f'{stopcolor}')

print(f"O número {numero} foi divisível {tot} vezes")
if tot == 2:
    print("Por isso ele é um número primo")
else:
    print("Por isso ele não é um número primo")