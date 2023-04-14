# Exercício Python 33: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
menor = ''
maior = ''
if n1 < n3 < n2:
    menor = n1
    maior = n2
elif n2 < n1 < n3:
    menor = n2
    maior = n3
elif n3 < n2 < n1:
    menor = n3
    maior = n1
print(f"O maior número é {maior} o menor número é {menor}")
