# Faça um algoritmo que leia o preço de um produto e
# mostre seu novo preço, com 5% de desconto.

precoproduto = float(input("Qual é o preço do produto?: R$"))
desconto = precoproduto * 0.5
print(f"O preço do produto com desconto é: R${precoproduto - desconto:.2f}")
