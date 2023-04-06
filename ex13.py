# Exercício Python 13: Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual é o salário do funcionário?: "))
aumento = salario * 0.15

print(f"O salário do funcionário com aumento é R${salario + aumento:.2f}")