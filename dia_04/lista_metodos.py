#metodo append - metodo que acrescenta valores a uma lista
# Listas sáo objetos mutaveis
# Atenção!!!! Strings não são mutaveis, se ocorre a alteração de uma string, o python cria uma copia dela e apresenta a nova versão
#%%
idades = [17, 32, 56, 87]
print(idades)

#%%
idades.append(32)
print(idades)

#%%
#lista vazia 

idades = []

while True:
    idade = input("Informe as idades: ")

    if idade == "":
        break
    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("media: ", media)
print("minimo: ", minimo)
print("maximo: ", maximo)
print("qtde: ", qtde)
# %%
