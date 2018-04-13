from random import randint

print("\n\nO computador vai pensar em um número de 1 a 100.\nTente adivinhar que número é esse!\nAtenção nas dicas!\n\n")

resposta = randint(1,101)

acertou = False

numero_tentativas = 0

while numero_tentativas < 10:

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
    print("\nVocê acertou!\n")
else:
    print("\nSuas tentativas acabaram! Tente de novo!\n")
