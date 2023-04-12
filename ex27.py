# Exercício Python 27: Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Informe seu nome: ")).strip()
nome = nome.split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome.[:9999]}")

