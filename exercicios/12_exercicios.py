#Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista:
#  laranja, cerveja, miojo, carvão, picanha.

lista_compras = ["laranja", "cerveja", "miojo", "carvão", "picanha"]
item_compra = input("Digite o item que você comprou: ")

if item_compra in lista_compras:
    print("Item comprado consta na lista")
else:
    print("Item não encontrado na lista")