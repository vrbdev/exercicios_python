#Peça a idade e diga se o voto é: Obrigatório (18 a 70), Facultativo (16-17 ou +70), Negado (<16)
# > maior
# < menor
idade = int(input("Informe sua idade: "))

if idade >= 18 and idade <= 69:
    print("O voto é obrigatorio!") 

elif idade >= 70:
    print("O voto é facultativo")

elif idade == 16 or idade == 17:
    print("O voto é facultativo")

else:
    idade <= 15
    print("Não tem idade para votar ainda")

 