import forca
import main

def escolhe_jogo():
    print("")
    print("*********************************")
    print("*** Bem vindo, vamos jogar ?! ***")
    print("******** Escolha um jogo ********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo ? "))

    if (jogo == 1):
        forca.jogar()
    elif (jogo == 2):
        main.jogar()

    print("FIM!")

if (__name__ == "__main__"):
    escolhe_jogo()