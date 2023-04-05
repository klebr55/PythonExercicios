# Exercício Python 4: Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

nomevariavel = input("Qual será o tipo da variável?\n===================================\n[Digite alguma palavra p/ "
                     "(string)\nou digite um número p/ (int, bool)]: ")

print("===================================")

print(f"O tipo da variável é: {type(nomevariavel)}")

if nomevariavel.islower():
    print(f"Ela está em minúsculo?: Sim, ela está")
else:
    print(f"Ela está em minúsculo?: Não, ela não está")

if nomevariavel.isupper():
    print(f"Ela está em maiúsculo?: Sim, ela está em maiúsculo")
else:
    print(f"Ela está em maiúsculo?: Não, ela não está em maiúsculo")

if nomevariavel.istitle():
    print(f"As letras iniciais estão em maiúsculo?: Sim, elas estão")
else:
    print("As letras iniciais estão capitalizadas?: Não, elas não estão")

if nomevariavel.isnumeric():
    print("É numérico?: Sim")
else:
    print("É numérico?: Não")

if nomevariavel.isalnum():
    print("É alfanumérico?: Sim")
else:
    print("É alfanumérico?: Não")

if nomevariavel.isspace():
    print("Possui espaços?: Sim")
else:
    print("Possui espaços?: Não")

if nomevariavel.isalpha():
    print("É alfabético?: Sim")
else:
    print("É alfabético?: Não")