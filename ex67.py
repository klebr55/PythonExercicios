# Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print(f"{'-=' * 45}"
      f"\n{'-' * 35}Gerador de Tabuada V3.0{'-' * 32}")
contador = 1
while True:
    numero = int(input(f"{'-=' * 45}"
                       f"\nDigite um valor para a sua tabuada "
                       f"\n[Digite um valor negativo para parar o programa]: "))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f"{numero} x {c:2} = {numero * c}")
print("Finalizando o programa...")