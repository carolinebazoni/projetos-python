# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input("Qual o salário? R$ "))
aumento = float(input("Qual o aumento? "))
novoSalario = salario + (salario*aumento)/100
print("Com o aumento de {}%, o salário fica R$ {}.".format(aumento, novoSalario))
