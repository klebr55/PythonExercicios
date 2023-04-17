# Exercício Python 22: Crie um programa que
# leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

from time import sleep

nome = str(input("Qual é o seu nome completo?: ")).strip()
print("Um momento, estou analisando seu nome...")
sleep(2)
print("Contando quantas letras tem...")
sleep(1)
print("Identificando qual é o primeiro nome...")
sleep(1)
print("Quase pronto...")
sleep(1)
print("Ok, obtive os seguintes dados: ")
sleep(0.5)
print(f"Seu nome todo em maiúsculo é: {nome.upper()}")
print(f"Seu nome todo em minúsculo é: {nome.lower()}")
dividido = nome.split()
print(f"Seu nome tem ao todo: "
      f"{len(nome) - nome.count(' ')}"
      f" letras")
print(f"Seu primeiro nome é {dividido[0]} e possui: {len(dividido[0])} letras")
