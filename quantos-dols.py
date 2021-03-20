# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dolar = float(input("Quanto vale o dólar americano hoje? R$ "))
dinheiro = float(input("Quanto dinheiro você tem na carteira? R$ "))

print("Você pode comprar US$ {:.2f} dólares.".format(dinheiro/dolar))