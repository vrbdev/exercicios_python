#Faça um programa que vende uma garrafa de água:
#Se o cliente escolher água mineral natural, será cobrado R$1,50
#Se o cliente escolher água mineral com gás, será cobrado R$2,50

# colocar """ possibilita escrever texto
texto = """
Escolha a sua água
(1) água mineral natural
(2) água mineral com gás
"""
opcao = input(texto)

if opcao == "1":
    print("sua conta deu R$1,50")

elif opcao == "2":
    print("sua conta deu R$2,50")

else:
    print("Valor informado está incorreto")


# outra opção de codigo

texto = """
Escolha a sua água
(1) água mineral natural
(2) água mineral com gás
"""
opcao = input(texto)

conta = 0
if opcao == "1":
    conta = 1.5

elif opcao == "2":
    conta = 2.5

if conta == 0:
    print("Valor informado está incorreto")

else:
    print("Sua conta é: R$", conta)
