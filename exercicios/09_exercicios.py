#Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), copo (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago
import sys

tx_sorvete = """
Tipo de sorvete:
 casquinha (R$1,00), 
 cascao (R$2,50), 
 copo (R$4,00)
"""
op_sorvete = input(tx_sorvete)
valor_sorvete = 0 

if op_sorvete == "casquinha":
    valor_sorvete = 1.0

elif op_sorvete == "cascao":
    valor_sorvete = 2.5

elif op_sorvete == "copo":
    valor_sorvete = 4.0

if valor_sorvete == 0: 
     print("Valor informado está incorreto")
     sys.exit()

tx_sabor = """ 
Sabor do sorvete: morango, creme, chocolate
 """
op_sabor = input(tx_sabor)

if op_sabor == "morango" or op_sabor == "creme" or op_sabor == "chocolate":
    pass
else:
    print("sabor invalido")
    sys.exit()

tx_cobertura =  """
Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
"""

op_cobertura = input(tx_cobertura)
valor_cobertura = 0

if op_cobertura == "Caramelo":
    valor_cobertura = 1.5

elif op_cobertura == "morango":
    valor_cobertura = 1.5

elif op_cobertura == "chocolate":
    valor_cobertura = 1.5

elif op_cobertura == "sem cobertura":
    valor_cobertura = 0.0

if op_cobertura == 0: 
     print("Valor informado está incorreto")

else: 
    valor_total = valor_sorvete + valor_cobertura
    print(valor_total)
