# Exercício Python 43: Desenvolva uma lógica que leia o peso
# e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

print(f"{'-=' * 10}"
      f"\nCalculadora de IMC"
      f"\n{'-=' * 10}")

peso = float(input("\nMe informe seu peso: "))
altura = float(input("Me informe sua altura: "))
imc = peso / (altura**2)


if imc < 18.5:
    print(f"\nSeu IMC é de {imc:.2f}"
          f"\nCuidado, você está abaixo do peso!")
elif 18.5 < imc < 25:
    print(f"\nSeu IMC é de {imc:.2f}"
          f"\nParabéns, você está no peso ideal :)")
elif 25 < imc < 30:
    print(f"\nSeu IMC é de {imc:.2f}"
          f"\nCuide-se, você está com sobrepeso")
elif 30 < imc < 40:
    print(f"\nSeu IMC é de {imc:.2f}"
          f"\nCuidado! Você está com obesidade :(")
elif imc >= 40:
    print(f"\nSeu IMC é de {imc:.2f}"
          f"\nPor favor, cuide-se, você está com obesidade mórbida")