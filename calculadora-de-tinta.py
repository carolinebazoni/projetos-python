# faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = float(largura*altura)
tinta = float(area/2)
print("A área da parede é {}m² e será necessário {} litros de tinta para pintá-la.".format(area, tinta))
