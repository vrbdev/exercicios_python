# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = int(input("Informe um numero inteiro: "))

raiz = numero ** (1/2) #pode ser tambem numero ** 0.5
raiz = round(raiz, 4)
print("A raiz quadrada de", numero, "é: ", raiz)