# Exercício Python 37: Escreva um programa em Python que leia um número
# inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número inteiro: "))
opcao = int(input("Escolha uma das bases para conversão: "
                  "\n[ 1 ] converter para BINÁRIO"
                  "\n[ 2 ] converter para OCTAL"
                  "\n[ 3 ] converter para HEXADECIMAL"
                  "\nSua opção: "))
numerobinario = bin(numero).replace("0b", "")
numerooctal = oct(numero).replace("0o", "")
numerohexadecimal = hex(numero).replace("0x", "")

if opcao == 1:
    print(f"{numero} convertido para BINÁRIO é {numerobinario}")
elif opcao == 2:
    print(f"{numero} convertido para OCTAL é {numerooctal}")
elif opcao == 3:
    print(f"{numero} convertido para HEXADECIMAL é {numerohexadecimal}")