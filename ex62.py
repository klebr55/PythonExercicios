# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
        total += mais
        while cont <= total:
                print(f"{termo} -> ", end="")
                termo += razao
                cont += 1
        print("Pausa")
        mais = int(input(f"Quantos termos você quer mostrar a mais?: "))
print(f"Progressão finalizada com {cont} termos mostrados")