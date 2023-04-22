# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.
opcao = ''
contador = 0
while opcao != 'N':
    primeirotermo = int(input("Digite o primeiro termo: "))
    razao = int(input("Digite a razão: "))
    termo = primeirotermo
    while contador <= 10:
        print(f"{termo} -> ", end='')
        termo += razao
        contador += 1
    contador = 0
    print('Acabou')
    opcao = str(input(f"Quer mais termos? [S/N]: ")).strip().upper()
    if 'S' in opcao:
        opcao = 'S'
        print(f"Ok, pode escolher ^^")
    elif 'N' in opcao:
        opcao = 'N'
        print(f"Ok, finalizando o programa...")
    else:
        while 'SN' not in opcao:
            print(f"Digite apenas 'S' para sim ou 'N' para não.")
            opcao = str(input(f"Quer mais termos? [S/N]: ")).strip().upper()