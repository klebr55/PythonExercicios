# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input(f"Diga o peso da {pessoas}° pessoa: "))
    if peso == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < maior:
        menor = peso
print(f"O maior peso foi {maior}kg e o menor peso foi {menor}kg")