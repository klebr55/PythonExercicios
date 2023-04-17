# Exercício Python 36: Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o valor da casa, o salário
# do comprador e em quantos anos ele vai pagar. A prestação mensal não pode
# exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input("Qual é o valor da casa?: "))
salario = float(input("Qual é o seu salário?: "))
anosparapagar = int(input("Quantos anos de financiamento?: "))

prestacao = (valorcasa / 12) / anosparapagar

if prestacao > (salario * 0.3):
    print(f"Para pagar uma casa de R${valorcasa:.2f} "
          f"em {anosparapagar} anos a prestação será de R${prestacao:.2f}"
          f" \nEmpréstimo não pode ser concedido")
else:
    print(f"Para pagar uma casa de R${valorcasa:.2f} "
          f"em {anosparapagar} anos a prestação será de R${prestacao:.2f}"
          f" \nEmpréstimo pode ser concedido!")