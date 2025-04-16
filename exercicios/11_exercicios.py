#Faça um programa que verifique se a pessoa pertence à família "santos" ou “silva”.

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")

if sobrenome == "santos":
    print("Você pertence a familia santos!")

elif sobrenome == "silva":
    print("Você pertence a familia silva!")

else:
    print("você pertence a outra familia")

