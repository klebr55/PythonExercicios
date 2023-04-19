# Exercício Python 51: Desenvolva um programa que leia
# o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
print(f"{'-=' * 17}"
      f"\nOs 10 primeiros termos de uma PA"
      f"\n{'-=' * 17}")
primeirotermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
decimo = primeirotermo + (10 - 1) * razao

for c in range(primeirotermo, decimo + razao, razao):
    print(f"{c} ->", end=' ')
print("Acabou")