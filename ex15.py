# Exercício Python 15: Escreva um programa que pergunte a quantidade de
# Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60
# por dia e R$0,15 por Km rodado.

kmpercorridos = float(input("Quantos KM o teu carro alugado percorreu?: "))
diasalugados = int(input("Por quantos dias você alugou o carro?: "))
precokm = (kmpercorridos * 0.15)
precodiasalugados = 60
print(f"Você percorreu por {kmpercorridos}km"
      f"\ne ficou {diasalugados} com o carro."
      f"\no preço final será: R${precokm + (diasalugados * 60)}")
