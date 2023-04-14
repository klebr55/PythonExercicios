# Exercício Python 31: Desenvolva um programa que pergunte a
# distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para
# viagens mais longas.

distanciaviagem = int(input("Qual foi a distância da viagem?: "))
if distanciaviagem <= 200:
    print(f"Você está prestes a começar uma viagem de "
          f"{distanciaviagem} KM e será cobrado em R${distanciaviagem * 0.50:.2f}")
else:
    print(f"Você está prestes a começar uma viagem de "
          f"{distanciaviagem} KM e será cobrado em R${distanciaviagem * 0.45:.2f}")