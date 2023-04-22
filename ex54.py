# Exercício Python 54: Crie um programa que leia o ano de
# nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

import datetime
contadormaior = 0
contadormenor = 0
for pessoas in range(1, 8):
    anonascimento = int(input(f"Qual é o ano de nascimento da {pessoas}° pessoa?: "))
    idade = datetime.date.today().year - anonascimento
    if idade >= 18:
        contadormaior += 1
    else:
        contadormenor += 1
print(f"Das 7 pessoas consultadas, {contadormenor} são menores de idade e "
      f"{contadormaior} são maiores de idade.")
