#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input("Qual o preço do produto? R$ "))
porcentagemDesconto = float(input("Qual a porcentagem de desconto? "))
desconto = (preco*porcentagemDesconto)/100
novoPreco = preco - desconto
print("O desconto é de R$ {:.2f} e o novo preço é R$ {:.2f}.".format(desconto, novoPreco))
