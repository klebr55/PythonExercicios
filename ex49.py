# Exercício Python 49: Refaça o DESAFIO 9, mostrando a
# tabuada de um número que o usuário escolher, só que
# agora utilizando um laço for.

numero = int(input("Digite um número para criar "
                   "sua tabuada: "))
for n in range(1, 11):
    print(f"{numero} x {n:2} = {numero * n:2}")