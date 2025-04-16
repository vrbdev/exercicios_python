# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de garrafas de água


texto = """
Escolha a sua água
(1) água mineral natural R$1,50
(2) água mineral com gás R$2,50
"""
opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5

elif opcao == "2":
    valor_item = 2.5

if valor_item == 0: 
     print("Valor informado está incorreto")

else:
    qtde = int(input("Quantas garrafas?"))
    valor_total = valor_item * qtde

    print("Sua compra deu um valor de R$", valor_total)