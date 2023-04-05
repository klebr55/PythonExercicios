#Exercício Python 06: Crie um algoritmo que leia um número e
# mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

numero = int(input("Digite um número para ver seu dobro"
                   "\ntriplo, e sua raíz quadrada: "))
print(f"O dobro de {numero} é: {numero * 2}"
      f"\nO triplo de {numero} é: {numero * 3}"
      f"\nA raiz quadrada de {numero} é: {sqrt(numero)}")