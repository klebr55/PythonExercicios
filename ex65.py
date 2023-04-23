# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = 0
contador = 0
somador = 0
maior = 0
menor = 0
opcao = ''
while 'N' not in opcao:
    numero = int(input("Digite um número: "))
    maior = numero
    menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    somador += numero
    contador += 1
    opcao = str(input("Quer continuar?: ")).strip().upper()
    if 'S' in opcao:
        opcao = 'S'
    elif 'N' in opcao:
        opcao = 'N'
    else:
        opcao = None
        while opcao is None:
            print("Digite apenas 'S' para sim ou 'N' para não.")
            opcao = str(input("Quer continuar?: ")).strip().upper()
            if 'S' in opcao:
                opcao = 'S'
            elif 'N' in opcao:
                opcao = 'N'
            else:
                opcao = None
print(f"Foram contabilizados {contador} números."
      f"\nA média entre todos os valores é {somador / contador:.0f}"
      f"\nO maior número é: {maior}"
      f"\nE o menor número é: {menor}")