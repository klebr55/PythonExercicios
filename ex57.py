# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.


nome = str(input("Qual é seu nome?: "))
sexo = str(input(f"Olá, {nome}. Qual é o seu sexo? [M/F]:")).strip().upper()
while sexo not in 'mMfF':
    sexo = str(input(f"Dados inválidos, por favor digite somente [M ou F]: ")).strip().upper()
    if 'M' in sexo:
        sexo = 'M'
    elif 'F' in sexo:
        sexo = 'F'
    else:
        print("Digite apenas ['M' ou 'F'] "
              "(M para Masculino e F para Feminino)")
if sexo == 'M':
    sexo = 'Masculino'
elif sexo == 'F':
    sexo = 'Feminino'
print(f"O sexo de {nome} é {sexo}")



