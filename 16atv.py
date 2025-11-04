"""
16 - Escreva um programa que pede que o usuário dê entrada em dois valores, em seguida,
exiba em tela o resultado da soma,subtração,multiplicação e divisão desses números:
"""
num1 = input("Digite um número:")
num2 = input("Digite o segundo número:")
num1= int(num1)
num2= int(num2)

resultado1 = (num1+num2)
print(f"A soma desses números é: {resultado1}",type(resultado1))
resultado2 = (num1*num2)
print(f"A multiplicaçã desses números é :{resultado2} ",type(resultado2))
resultado3= (num1/num2)
print(f"A divisão desses números é {resultado3}",type(resultado3))
