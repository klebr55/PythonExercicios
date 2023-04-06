# Exercício Python 11: Faça um programa que leia a largura e a altura de uma
# parede em metros, calcule a sua área e a quantidade de tinta necessária para
# pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larguraparede = float(input("Me diga a largura da parede: "))
alturaparede = float(input("Me diga a altura da parede: "))
area = larguraparede * alturaparede
tinta = 2

print(f"Sua parede possui {larguraparede}m de largura e {alturaparede}m de altura"
      f"\nPara pintar os {area}m² da parede você vai precisar de {area / tinta:.1f}l de tinta")
