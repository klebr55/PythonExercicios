# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo
# teclado e mostre na tela a sua porção Inteira.

import math

numero = float(input("Digite um número quebrado para ver sua porção inteira: "))
porcaointeira = math.trunc(numero)

print(f"A porção inteira de {numero} é: {porcaointeira}")

