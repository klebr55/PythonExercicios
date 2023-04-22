# Exercício Python 060: Faça um programa que
# leia um número qualquer e mostre o seu fatorial. Exemplo:

# 5! = 5 x 4 x 3 x 2 x 1 = 120

import math
opcao = ''
while opcao != 'N':
    numero = int(input("Digite um número: "))
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} é: {numero}! =", end='')
    c = numero
    while c > 0:
        print(f" {c}", end='')
        if c > 1:
            print(" x", end='')
        else:
            print(f" = {fatorial}", end='')
        c -= 1
    opcao = str(input("\nQuer continuar? [S/N]: ")).strip().upper()
print("Ok, finalizando o programa :)...")