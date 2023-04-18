# Exercício Python 041: A Confederação Nacional de Natação
# precisa de um programa que leia o ano de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER

from datetime import datetime
anonascimento = int(input("Qual é o seu ano de nascimento?: "))
idade = datetime.now().year - anonascimento
if anonascimento < 9:
    print(f"De acordo com sua idade, você é um atleta mirim")
elif 9 < idade < 14:
    print(f"De acordo com sua idade, você é um atleta infantil")
elif 14 < idade < 19:
    print(f"De acordo com sua idade, você é um atleta júnior")
elif 19 < idade < 25:
    print(f"De acordo com sua idade, você é um atleta sênior")
elif idade >= 25:
    print(f"De acordo com sua idade, TU É MUITO FODA MEU PARCEIRO"
          f"\nTU É NÍVEL MASTER!")
