# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a
# ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.

from time import sleep
from random import shuffle

lista = []

print("==========================================================="
      "\nO professor quer sortear a ordem de apresentação dos alunos"
      "\n===========================================================")

for i in range(4):
    alunos = str(input("Informe o nome dos alunos: "))
    lista.append(alunos)
print(f"O professor está embaralhando...")
sleep(5)
print("3...")
sleep(1)
print("2...")
sleep(1)
print("1...")
sleep(1)
print("PRONTO!")
sleep(0.5)
shuffle(lista)

print(f"A ordem de apresentação da lista será: {lista}")