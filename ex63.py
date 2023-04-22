# Exercício Python 63: Escreva um programa que leia um número
# N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8
# t1 = 0 | t2 = 1 | t3 = t1 + t2

print(f"{'-=' * 10}"
      f"\nSequência Fibonacci"
      f"\n{'-=' * 10}")
numero = int(input("Digite um número: "))
termo1 = 0
termo2 = 1
cont = 3
print(f"{termo1} -> {termo2} -> ", end="")
while cont <= numero:
    termo3 = termo1 + termo2
    print(f"{termo3} -> ", end="")
    termo1 = termo2
    termo2 = termo3
    cont += 1
print("fim")