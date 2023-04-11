# Nessa aula, vamos aprender operações com String no Python.
# As principais operações que vamos aprender são o Fatiamento
# de String, Análise com len(), count(), find(), transformações
# com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

'''frase = 'Curso em Vídeo Python'
print(frase[3:15])'''

'''frase = 'Curso em Vídeo Python'
print(frase[3:15:2])'''

'''frase = 'Curso em Vídeo Python'
print(frase[3:15:2])'''

"""frase = 'Curso em Vídeo Python'
print(frase.count('o'))"""  # conta quantas letras "o" possuem na string
                                # na variável frase

'''frase = 'Curso em Vídeo Python'
print(frase.upper().count('O'))'''  # conta quantas letras "o" em maiúsculo possuem na string
                                    # da variável frase

'''frase = 'Curso em Vídeo Python'
print(len(frase))'''  # mede o comprimento da frase

'''frase = '   Curso em Vídeo Python   '
print(len(frase.strip()))'''  # remove os espaços da frase

'''frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))'''  # troca a palavra 'Python' por 'Android'

'''frase = 'Curso em Vídeo Python'
print('Curso' in frase)'''  # diz se a tal palavra está na string

'''frase = 'Curso em Vídeo Python'
print(frase.find('Curso)'''  # mostra em qual posição está a palavra

frase = 'Curso em Vídeo Python'
dividido = frase.split()  # divide a frase
print(dividido[0])  # seleciona a palavra que você quer