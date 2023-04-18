# Exercício Python 39: Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com a sua idade, se ele ainda vai
# se alistar ao serviço militar, se é a hora exata de se alistar ou se
# já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.

from datetime import datetime

anonascimento = int(input("Ano de nascimento: "))
idade = datetime.now().year - anonascimento
alistamento = 18 - idade
print(f"Quem nasceu em {anonascimento} tem {idade} anos em {datetime.now().year}")
if idade < 18:
    print(f"Ainda faltam {alistamento} anos para o alistamento.")
    print(f"Seu alistamento será em {datetime.now().year + alistamento}")
elif idade == 18:
    print(f"Você precisa realizar o alistamento imediatamente!"
          f"\nRealize seu alistamento online pelo site www.alistamento.eb.mil.br"
          f"\nEsteja em dia com sua pátria, jovem :)")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {alistamento - (alistamento * 2)} anos.")
    print(f"Seu alistamento foi em {datetime.now().year + alistamento}")

