# O formato \033[0:30:41m é uma sequência de escape ANSI que pode ser
# usada para definir cores e estilos de texto no terminal. A sequência
# é composta de três números separados por dois pontos e um caractere 'm'
# no final.

# Aqui está uma descrição de cada parte da sequência:

# \033: código de escape ANSI que indica o início de uma sequência de controle.

# 0: define o estilo padrão do texto. Este valor é opcional, pois 0 é o valor padrão.

# Além de 0, que define o estilo padrão do texto, existem outros valores
# que podem ser usados para definir estilos de texto em uma sequência de
# escape ANSI. Aqui estão alguns exemplos:

# 1: define o texto em negrito.
# 2: define o texto em um estilo "desbotado" ou "faint".
# 3: define o texto em itálico.
# 4: define o texto sublinhado.
# 5: define o texto piscante.
# 7: inverte as cores do texto e do fundo.
# 8: oculta o texto.

# Cada um desses valores pode ser usado em uma sequência de escape ANSI para
# aplicar o estilo correspondente ao texto. Por exemplo, para definir o texto
# em negrito e na cor vermelha, você pode usar a sequência de escape ANSI \033[1;31m.

# Lembre-se de que nem todos os terminais suportam todos os estilos de texto.
# Alguns estilos, como "desbotado" e "itálico", podem não ser suportados em alguns
# terminais. Portanto, é importante testar as sequências de escape em diferentes
# terminais para garantir que elas produzam o efeito desejado.

# 30: define a cor do texto como preto. Outros valores para definir a cor do texto incluem:
# 31: vermelho
# 32: verde
# 33: amarelo
# 34: azul
# 35: magenta
# 36: ciano
# 37: branco

# 41: define a cor de fundo do texto como vermelho.
# Outros valores para definir a cor de fundo incluem:
# 40: preto
# 42: verde
# 43: amarelo
# 44: azul
# 45: magenta
# 46: ciano
# 47: branco
# m: indica o fim da sequência de controle.

# Define as cores em variáveis
preto = '\033[0;30m'
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
azul = '\033[0;34m'
magenta = '\033[0;35m'
ciano = '\033[0;36m'
branco = '\033[0;37m'
stopcolor = '\033[m'

# Define os estilos em variáveis
negrito = '\033[1m'
italico = '\033[3m'
sublinhado = '\033[4m'
piscante = '\033[5m'
inverso = '\033[7m'
oculto = '\033[8m'

# Exemplo de uso das variáveis
print(vermelho + negrito + 'Texto em vermelho e negrito' + oculto)
