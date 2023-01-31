print("*********************************")
print("Bem vindo ao jogo, vamos jogar ?!")
print("*********************************")
numero_chutado = 43
tentativas = 3
rodadas = 1

while (rodadas <= tentativas):

    chutando = input("Qual o valor do seu chute ? ")
    # O input é a mesma coisa que o prompt
    print("Rodada  {} de  {}".format(rodadas, tentativas))
    # Aqui estamos usando a função interpolada onde usamos os {} para colocar um valor dentro
    # e para que esse valor seja inserido usamos o .format() e dentro dele colocamos os valores que queremos
    # que apareça, deixando o código mais organizado e limpo.
    print("Você chutou: ", chutando)

    chute   = int(chutando)
    maior   = chute > numero_chutado
    menor   = chute < numero_chutado
    acertou = chute == numero_chutado

    if (acertou):
    # Possui a opção de digitar os if e else elif sem usar os (), tanot que foi utilizado os dois modelos para relembrar essa informação
        print("*********************************")
        print("**** Você acertou!  PARABÉNS ****")
        print("*********************************")
    else:
        if maior:
            print("Você errou! O seu chute é maior que o numero sorteado")
        elif menor:
            print("Você errou! O seu chute é menor que o numero sorteado")
            print("*****************************************************")
    rodadas = rodadas + 1

print("Jogo encerrado")
