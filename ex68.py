# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint
from time import sleep

contvencedor = 0
contperdedor = 0
contador = 0
continuar = ''
while True:
    contador += 1
    escolha = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()
    if 'P' in escolha:
        escolha = 'P'
    elif 'I' in escolha:
        escolha = 'I'
    else:
        escolha = None
        while escolha is None:
            print(f"Digite apenas 'P' p/ PAR ou 'I' p/ ÍMPAR.")
            escolha = str(input("Par ou Ímpar? [P/I]: ")).strip().upper()
            if 'P' in escolha:
                escolha = 'P'
            elif 'I' in escolha:
                escolha = 'I'
            else:
                escolha = None
    jogador = int(input("Ok, digite seu número: "))
    print("\nUm momento, o computador está pensando no número em que vai jogar...")
    sleep(2)
    print("\nPC: Estou pronto, aqui vamos!")
    sleep(1)
    pc = randint(1, 50)
    if 'P' in escolha:
        if (jogador + pc) % 2 == 0:
            print(f"\nVocê escolheu: {jogador} e o PC escolheu: {pc}"
                  f"\nVocê venceu!")
            contvencedor += 1
        else:
            print(f"\nVocê escolheu: {jogador} e o PC escolheu: {pc}"
                  f"\nVocê perdeu!")
            contperdedor += 1
    elif 'I' in escolha:
        if (jogador + pc) % 2 == 1:
            print(f"\nVocê escolheu: {jogador} e o PC escolheu: {pc}"
                  f"\nVocê venceu!")
            contvencedor += 1
        else:
            print(f"\nVocê escolheu: {jogador} e o PC escolheu: {pc}"
                  f"\nVocê perdeu!")
            contperdedor += 1
    continuar = str(input(f"\nVocê quer continuar? [S/N]: ")).strip().upper()
    if 'S' in continuar:
        continuar = 'S'
    elif 'N' in continuar:
        continuar = 'N'
        break
    else:
        continuar = None
        while continuar is None:
            print(f"Digite apenas 'S' p/ sim ou 'N' p/ não.")
            continuar = str(input(f"\nVocê quer continuar? [S/N]: ")).strip().upper()
            if 'S' in continuar:
                continuar = 'S'
            elif 'N' in continuar:
                continuar = 'N'
            else:
                continuar = None
print(f"\n{'-=' * 10} "
      f"\nRESULTADOS "
      f"\n{'-=' * 10}"
      f"\nVocê jogou {contador} vezes com o PC"
      f"\nGanhou {contvencedor} vezes do PC"
      f"\nE perder {contperdedor} vezes para o PC")