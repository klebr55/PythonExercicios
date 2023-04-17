# Exercício Python 038: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

if numero1 > numero2:
    maior = numero1
    print("O primeiro valor é maior")
elif numero2 > numero1:
    maior = numero2
    print("O segundo valor é maior")
elif numero1 == numero2:
    print("Os dois valores são iguais")