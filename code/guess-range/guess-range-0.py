from random import randint

print("\n\nO computador vai pensar em um número de 1 a 10.\nTente adivinhar que número é esse!\n\n")

resposta = randint(1,11)

tentativa = int(input("Qual o seu chute? "))

if (tentativa > resposta):
    print("Errou! Era um número menor!\n")
elif (tentativa < resposta):
    print("Errou! Era um número maior!\n")
else:
    print("Você acertou!\n")

