import random
import forca
import main

# o random.random é para gerar um numero aleatório
# o random.randrange (x, y) é para gerar um numero aleatório do valor x ao y, mas o valor do y vai ser 1 a menos

print("*********************************")
print("*** Bem vindo, vamos jogar ?! ***")
print("******** Escolha um jogo ********")
print("*********************************")

print("(1) Forca (2) Adivinhação")
jogo = int(input("Qual jogo ?"))

if (jogo == 1):
    print("Jogando jogo da forca")
elif (jogo == 2):
    print("Jogando adivinhação")
