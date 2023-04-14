# Exercício Python 30: Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input("Digite um número e eu direi se ele é par ou ímpar: "))
if numero % 2 == 0:
    print(f"O número {numero} par")
else:
    print(f"O número {numero} é ímpar")