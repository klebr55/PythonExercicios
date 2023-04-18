# Exercício Python 040: Crie um programa que leia duas notas de um
# aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:

# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO

nota = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota + nota2) / 2

if media < 5.0:
    print(f"Sua média foi de: {media:.2f}"
          f"\nREPROVADO!")
if 5.0 < media < 6.9:
    print(f"Sua média foi de: {media:.2f}"
          f"\nVOCÊ ESTÁ DE RECUPERAÇÃO!")
elif media >= 7.0:
    print(f"Sua média foi de: {media:.2f}"
          f"\nPARABÉNS! VOCÊ PASSOU")