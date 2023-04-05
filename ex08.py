#Exercício Python 8: Escreva um programa que leia um valor em
# metros e o exiba convertido em centímetros e milímetros.

metros = int(input("Digite um valor em METROS que eu o"
                   "\nconverterei em CENTÍMETROS"
                   " e em MILÍMETROS: "))

print(f"O valor que você digitou é: {metros}m"
      f"\nem centímetros ele é: {metros * 100}cm"
      f"\nem milímetros ele é: {metros * 1000}mm")
