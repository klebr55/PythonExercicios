# Exercício Python 33: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))

# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c

# Verificando quem é maior
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c

print(f"O maior número é {maior} o menor número é {menor}")
