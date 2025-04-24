#Faça um programa que receba 4 alturas usando um laço de repetição 
# e realize a soma dessas altura
#%%
#WHILE
soma = 0 #valor final
qtde_entradas = 4 # o contador de entradas 

while qtde_entradas > 0:
    altura = float(input("Informe a altura: "))
    soma += altura 
    qtde_entradas -= 1

print("Soma das alturas é: ", soma)

# FOR
#%%

soma = 0 #valor final
qtde_entradas = 4 # o contador de entradas 

for i in range(qtde_entradas): # mesma coisa que range(0, 4) ou  range(0, qtde_entradas)
    altura = float(input("Informe a altura: "))
    soma += altura
print("Soma das alturas é: ", soma)

# %%
