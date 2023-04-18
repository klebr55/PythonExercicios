# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

r1 = float(input("Diga o comprimento da primeira reta: "))
r2 = float(input("Diga o comprimento da segunda reta: "))
r3 = float(input("Diga o comprimeto da terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Pode formar um triângulo", end='')
    if r1 == r2 == r3:
        print("Pode formar um triângulo EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("Pode formar um triângulo ESCALENO")
    else:
        print("Pode formar um triângulo ISÓCELES")
else:
    print("Não pode formar um triângulo")