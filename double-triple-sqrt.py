#crie um algoritmo que leia um numero e mostre seu dobro, triplo e a raíz quadrada

numero = int(input("Digite um número: "))
print("O dobro de {} é {}, o triplo é {} e a raíz quadrada é {:.3f}.".format(numero, (numero * 2), (numero * 3), (numero ** (1/2))))