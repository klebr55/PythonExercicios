# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos
# e escrevendo na tela o nome do escolhido.

import random, time  # importa a biblioteca random e time

lista = []  # cria uma lista

print("==============================================================="
      "\nO professor irá sortear o nome de 4 alunos para apagar o quadro"
      "\n===============================================================")

# ======== início seção "for" ============

# estou utilizando o comando for para jogar
# 4 nomes na lista através do comando input na variável "alunos" que será gerado 4 vezes

for sorteio in range(4):
    alunos = str(input("\nDiga o nome dos alunos: "))
    lista.append(alunos)  # .append joga os nomes digitados na lista

# fim da seção "for"

# ======== fim da seção "for" ============

print("\nUm momento, o professor está sorteando os alunos...")

time.sleep(5)  # faz o programa esperar 5 segundos para pensar
lista = random.choice(lista)  # .choice escolhe aleatoriamente o objeto que
                                # você colocar dentro dos parenteses

print(f"\nO aluno {lista} foi escolhido para apagar o quadro :D")