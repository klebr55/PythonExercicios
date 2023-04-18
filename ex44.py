# Exercício Python 44: Elabore um programa que calcule o valor
# a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal

# – 3x ou mais no cartão: 20% de juros
print(f"{'-=' * 5} LOJAS SÓSHOP {'=-' * 5}")
valor = float(input("Preço das compras: "))
pagamento = int(input(f"Qual método de pagamento você quer utilizar?"
                      f"\n[1] à vista dinheiro/cheque"
                      f"\n[2] à vista no cartão"
                      f"\n[3] em até 2x no cartão"
                      f"\n[4] 3x ou mais no cartão"
                      f"\nQual é a opção?: "))
if pagamento == 1:
    print(f"Sua compra de R${valor:.2f} irá custar R${valor - (valor * 0.10):.2f}")
elif pagamento == 2:
    print(f"Sua compra de R${valor:.2f} irá custar R${valor - (valor * 0.05):.2f}")
elif pagamento == 3:
    print(f"Sua compra de R${valor:.2f} será dividida em 2 parcelas de R${valor / 2:.2f}")
elif pagamento == 4:
    parcelas = int(input(f"Quantas parcelas?: "))
    print(f"Sua compra de R${valor:.2f} será divida em {parcelas} parcelas"
          f"\nde R${valor / parcelas:.2f} COM JUROS")