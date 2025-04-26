#Escreva um programa que receba uma lista de numeros do usuario e conte 
# quantas vezes um numero especifico aparece na lista
#Solicite ao ususario um numero e exiba a contagem

#%%

lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input("Informa um numero: "))

contador = 0

for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de", numero, "na lista é:", contador)
# %%
