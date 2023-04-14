# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidadecarro = float(input("Qual é a velocidade do carro?: "))
multa = 7.00

if velocidadecarro > 80:
    print(f"Você foi multado por excesso de velocidade, a multa será de R${(velocidadecarro - 80) * multa:.2f}"
          f" \ntenha um ótimo dia, dirija com segurança!")
else:
    print(f"Parabéns, você está conforme a lei.")