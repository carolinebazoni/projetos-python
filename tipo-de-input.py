#faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele.

algo = input("Digite algo: ")
print("o tipo primitivo é ", type(algo))
print("Só tem espaços?", algo.isspace())
print("É um número?", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É alfanumérico?", algo.isalnum())
print("Está em maiúsculas?", algo.isupper())
print("Está em mínusculas?", algo.islower())
print("Está capitalizada?", algo.istitle())