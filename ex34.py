# Exercício Python 34: Escreva um programa que pergunte o
# salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual é o salário do funcionário?: "))

if salario > 1250.00:
    aumento = (salario * 0.10) + salario
    print(f"O salário do funcionário é R${salario:.2f} "
          f"seu aumento será de "
          f"10%, resultando então em um salário de: R${aumento:.2f}")
elif salario <= 1250.00:
    aumento2 = (salario * 0.15) + salario
    print(f"O salário do funcionário é R${salario:.2f} "
          f"seu aumento será de "
          f"15%, resultando então em um salário de: R${aumento2:.2f}")