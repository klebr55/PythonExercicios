# Exercício Python 050: Desenvolva um programa que leia seis
# números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
contador = 0
soma = 0
for c in range(1, 7):
    numero = int(input(f"Digite o {c}° número: "))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f"Você digitou {contador} números pares e a soma entre eles foi: {soma}")

