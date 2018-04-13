from random import randint

print("\n\nVocê terá de adivinhar um número que está dentro de uma faixa de valores! Que faixa é essa?\n")

min_valor = int(input("Menor valor: ")) 
max_valor = int(input("Maior valor: "))

print("\n\nO computador vai pensar em um número de "+ str(min_valor) +" a "+ str(max_valor) 
        +".\nTente adivinhar que número é esse!\nAtenção nas dicas!\n\n")

max_tentativas = int(input("Quantas vezes quer tentar? "))

max_partidas = int(input("E quantas vezes você quer jogar? "))

numero_partidas = 0

numero_acertos = 0

while numero_partidas < max_partidas :

    numero_partidas = numero_partidas + 1

    print("\n(*) Partida " + str(numero_partidas)+"\n")

    resposta = randint(min_valor, max_valor + 1)

    acertou = False

    numero_tentativas = 0

    while numero_tentativas < max_tentativas:

        numero_tentativas = numero_tentativas + 1

        print("=> Tentativa " + str(numero_tentativas))

        tentativa = int(input("Qual o seu chute? "))

        if (tentativa > resposta):
            print("Tente um número menor!\n")
        elif (tentativa < resposta):
            print("Tente um número maior\n")
        else:
            acertou = True
            break

    if acertou:
        numero_acertos = numero_acertos + 1
        print("\nVocê acertou!\n")
    else:
        print("\nSuas tentativas acabaram nesta partida!\n")

print("\n\n(*) Você já jogou todas as partidas e acertou " + str(numero_acertos) + "!")
