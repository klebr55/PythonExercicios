# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

contador = 0
somador = 0
while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero != 999:
        somador += numero
        contador += 1
    else:
        break
print(f"{contador} números foram contabilizados e a soma entre eles é: {somador}")