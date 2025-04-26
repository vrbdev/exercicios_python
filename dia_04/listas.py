
# %%

vivian = ["vivian", "rocha", True, 24, 2000.35]
print(vivian)
# %%
print(vivian[0])
# %%
print(vivian[5])
# %%

idades =[10, 12, 20, 52, 75, 31, 11, 7]
print("soma idades: ", sum(idades))

print("quantidade lista: ", len(idades))

print("media idades: ", sum(idades)/ len(idades))

# o LEN informa o tamanho da lista

print("menos idade: ", min(idades))

print("maior idade ", max(idades))
# %%

flavio = ["flavio borges",
         51, 
         True, 
         "casado",
         ["autonomo", "estudante", "bancario", "professor", "secretario"],
         [3000, 2000, 8000, 10000, 13000],
         ["vivian", "lilian", "emanuel"]]
print(len(flavio))

flavio[4][0]
# explicacao do flavio[4][0]
filhos = flavio[4]
primogenita = filhos[0]
print(primogenita)
#%%
tamanho = len(flavio)
pos = tamanho - 1
flavio[pos][0]
# %%

#fatiamento 
# pegar os seguintes dados da lista "flavio borges", 51, True, "casado"

flavio[0:4]
# %%

#duas ultimas posções no mercado de trabalho 
flavio[4][3:5]
# %%
#outra forma de fazer
flavio[4][-2:]
# %%
#sintaxe do slice
# [start : stop : step]

salarios = flavio[5]
print(salarios)

salarios[::2]

salarios[::-1]
# %%
