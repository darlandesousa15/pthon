print("*********************************")
print("Bem vindo ao jogo, vamos jogar ?!")
print("*********************************")
numero_chutado = 43

chutando = input("Qual o valor do seu chute ? ")
print("Você chutou: ", chutando)
chute = int(chutando)
if (chute == numero_chutado):
    print("*********************************")
    print("**** Você acertou!  PARABÉNS ****")
    print("*********************************")
else:
    print("Você errou :(")
print("Jogo encerrado")
