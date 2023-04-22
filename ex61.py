# Exercício Python 61: Refaça o DESAFIO 51, lendo o
# primeiro termo e a razão de uma PA, mostrando os 10
# primeiros termos da progressão usando a estrutura while.

print(f"{'-=' * 7}"
      f"\nGerador de PA"
      f"\n{'-=' * 7}")
primeirotermo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeirotermo
contador = 0
while contador <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    contador += 1
print("Acabou")
