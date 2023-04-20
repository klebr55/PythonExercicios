# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0
maior = 0
while opcao != 5:
    numero1 = int(input("Qual será o primeiro valor?: "))
    numero2 = int(input("Qual será o segundo valor?: "))
    while opcao != 4:
        opcao = int(input(f"{'=' * 6} Escolha uma opção {'=' * 6}"
                          f"\n[1] Somar"
                          f"\n[2] Multiplicar"
                          f"\n[3] Maior"
                          f"\n[4] Novos Números"
                          f"\n[5] Sair do programa"
                          f"\nEscolha sua opção: "))
        if opcao == 1:
            print(f"A soma entre {numero1} e {numero2} é: {numero1 + numero2}")
        elif opcao == 2:
            print(f"A multiplicação entre {numero1} e {numero2} é: {numero1 * numero2}")
        elif opcao == 3:
            if numero1 > numero2:
                maior = numero1
                print(f"O maior número é o número {numero1}")
            elif numero1 < numero2:
                maior = numero2
                print(f"O maior número é o número {numero2}")
            elif numero1 == numero2:
                print(f"Os números possuem o mesmo valor")
        elif opcao == 4:
            print(f"Ok, pode escolher seus novos números :)")
        elif opcao == 5:
            opcao = 52
            print(f"Ok, saindo do programa...")
