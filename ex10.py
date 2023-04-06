#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

dinheiro = float(input("Quanto dinheiro você tem na carteira?: "))
dolar = 5.07

print(f"De acordo com a cótação do dólar atual,"
      f"\ncom R$ {dinheiro:.2f} você pode comprar U$ {dinheiro / dolar:.2f} dólares")