import random
import jogos
# o random.random é para gerar um numero aleatório
# o random.randrange (x, y) é para gerar um numero aleatório do valor x ao y, mas o valor do y vai ser 1 a menos
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo, vamos jogar ?!")
    print("*********************************")

    print("")

    print("Deseja jogar novamente ? (1) Sim (2) Não (3) Voltar a seleção de jogos")
    restart = input("Selecione sua opção ")
    if (restart == "1"):
        jogar()
    elif (restart == "2"):
        print("*** Fim de Jogo ***")
    else:
        jogos.escolhe_jogo()

if (__name__ == "__main__"):
    jogar()
