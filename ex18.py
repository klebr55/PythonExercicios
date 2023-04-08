# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = int(input("Informe o ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo de {angulo}° tem o Seno de: {seno:.2f}"
      f"\nO ângulo de {angulo}° tem o Cosseno de: {cosseno:.2f}"
      f"\nO ângulo de {angulo}° tem a Tangente de: {tangente:.2f}")