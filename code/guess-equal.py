from random import randint

print(": ) \n\nOlá! Será que você é bom em adivinhar?\n\nO computador vai pensar em um número de 0 a 9 e você deverá dizer qual é!")

jogadas = int(input("=> Quantas vezes você quer jogar? "))

acertos = 0

for i in range (0, jogadas):

    print("\n(*) Jogada " + str(i + 1) + "\n")

    resposta = randint(0,9)

    print("O computador já pensou!\n")

    jogou = False

    while not jogou:

        tentativa = int(input("=> Qual o seu chute? "))

        if (tentativa < 0 or tentativa > 9):
            print("Só números de 0 a 9!")
        else:
            jogou = True
            if (tentativa == resposta):
                acertos = acertos + 1
                print("\nAcertou!")
            else:
                print("\nErrou! A resposta era " + str(resposta))
            break

print("\n\nVocê acertou " + str(acertos) + "!")
