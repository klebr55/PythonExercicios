# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input("Informe o comprimento do Cateto Oposto do Triângulo Retângulo: "))
ca = float(input("Informe o comprimento do Cateto Adjacente do Triângulo Retângulo: "))
tdepitagoras = (co**2) + (ca**2)
hip = math.sqrt(tdepitagoras)
print(f"O valor do comprimento da Hipotenusa é: {hip:.2f}")
