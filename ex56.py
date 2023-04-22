# Exercício Python 56: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais
# velho e quantas mulheres têm menos de 20 anos.

totidade = 0
nomemaioridade = 0
maioridade = 0
contmulher = 0
for pessoas in range(1, 5):
    nome = str(input(f"{'-' * 10} {pessoas}° pessoa {'-' * 10}"
                     f"\nNome: "))
    idade = int(input(f"Idade de {nome}: "))
    totidade += idade
    sexo = str(input(f"Sexo de {nome} [M/F]: ")).strip().upper()
    if 'M' in sexo:
        if idade == 1:
            idade = maioridade
            nome = nomemaioridade
        elif idade > maioridade:
            maioridade = idade
            nomemaioridade = nome
    if 'F' in sexo:
        if idade <= 20:
            contmulher += 1
media = totidade / pessoas
print(f"A média de idade do grupo é de {media} anos")
print(f"O homem mais velho tem {maioridade} anos e se chama {nomemaioridade}")
if contmulher >= 1:
    print(f"Ao todo são {contmulher} mulheres com menos de 20 anos")
else:
    print(f"Não foram listadas mulheres com menos de 20 anos")
