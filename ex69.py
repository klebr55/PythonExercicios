# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

from time import sleep

maioridade = 0
conthomens = 0
contmulheres = 0

while True:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        maioridade += 1
    sexo = 'RESET'
    while sexo == 'RESET':
        sexo = str(input("Digite seu sexo [M/F]: ")).strip().upper()
        if 'F' in sexo:
            sexo = 'F'
            if idade < 20:
                contmulheres += 1
        elif 'M' in sexo:
            sexo = 'M'
            conthomens += 1
        else:
            print("Opção errada, digite apenas 'M' para masculino e 'F' para feminino")
            sexo = 'RESET'
    opcao = 'RESET'
    while opcao == 'RESET':
        opcao = str(input("Você quer continuar? [S/N]: ")).strip().upper()
        print(f"{'-=' * 20}")
        if 'S' in opcao:
            opcao = 'S'
        elif 'N' in opcao:
            opcao = 'N'
            break
        else:
            opcao = 'RESET'
            print("Opção errada, digite apenas 'S' para sim e 'N' para não")
    if opcao == 'N':
        break
print(f"Apurando Resultados...")
sleep(5)
print(f"\nO Software contabilizou {maioridade} pessoas maiores de idade"
      f"\nO mesmo contabilizou também {conthomens} homens"
      f"\nE {contmulheres} mulheres com menos de 20 anos")