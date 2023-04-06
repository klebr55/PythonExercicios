# Exercício Python 14: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

celsius = int(input("Qual é a temperatura atual aí da sua cidade"
                    " em °Celsius?: "))
fahrenheit = (celsius * 1.8) + 32

print(f"A temperatura local da sua cidade em °Fahrenheit é: °{fahrenheit}")
