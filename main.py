import random
# o random.random é para gerar um numero aleatório

print("*********************************")
print("Bem vindo ao jogo, vamos jogar ?!")
print("*********************************")

numero_chutado = round(random.random() * 100)
tentativas = 8
rodadas = 1

# while (rodadas <= tentativas):
for rodadas in range (rodadas, tentativas + 1):
# O while e o incrementador de rodadas está comentado para utilizar o for
# for ... in range (..., ...): no lugar dos ... utilizar as variaveis e dentro do parenteses vc pode
# implementar 1 ou subtrair pois o valor final dentro dele é escluido por exemplo o valor final de tentativa é 3 então o 3 ñ vai fazer parte do loop por isso foi incrementado 1 para ficar 3 repetições e a 4 ser excluida
# for in range(start, stop, [step]) exemplificando os detalhes do for

    chutando = input("Qual o valor do seu chute ? Deve ser entre 1 e 100 ")
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


    if (chute < 1 or chute > 100):
        print("Valor incorreto, digite um chute entre 1 e 100")
        print("**********************************************")
        continue

    if (acertou):
    # Possui a opção de digitar os if e else elif sem usar os (), tanto que foi utilizado os dois modelos para relembrar essa informação
        print("*****************************************************")
        print("************** Você acertou!  PARABÉNS **************")
        print("*****************************************************")
        break
    else:
        if maior:
            print("Você errou! O seu chute é maior que o numero sorteado")
            print("************** ESCOLHA UM NÚMERO MENOR **************")
        elif menor:
            print("Você errou! O seu chute é menor que o numero sorteado")
            print("************** ESCOLHA UM NÚMERO MAIOR **************")
            print("*****************************************************")
    # rodadas = rodadas + 1

print("Jogo encerrado o número sorteado foi ", numero_chutado)
