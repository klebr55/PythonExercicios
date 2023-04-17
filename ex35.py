# Exercício Python 35: Desenvolva um programa que leia o comprimento de
# três retas e diga ao usuário se elas podem ou não formar um triângulo

print(f"{'-=' * 15}"
      f"\nAnalisador de Triângulos"
      f"\n{'-=' * 15}")
r1 = float(input("Qual o comprimento da primeira reta?: "))
r2 = float(input("Qual o comprimento da segunda reta?: "))
r3 = float(input("Qual o comprimento da terceira reta?: "))

# Verifica quem é o menor número
menor = r1
if r2 < r1 and r2 < r3:
    menor = r2
elif r3 < r1 and r3 < r2:
    menor = r3

# Verifica quem é o maior número
maior = r1
if r2 > r1 and r2 > r3:
    maior = r2
elif r3 > r1 and r3 > r2:
    maior = r3

# Verifica qual é número do meio
meio = r1
if menor < r2 < maior:
    meio = r2
elif menor < r3 < maior:
    meio = r3

if (menor + meio) >= maior:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")