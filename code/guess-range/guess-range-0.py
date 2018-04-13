from random import randint

print("\n\nO computador vai pensar em um número de 1 a 100.\nTente adivinhar que número é esse!\nAtenção nas dicas!\n\n")

resposta = randint(1,101)

tentativa = int(input("Qual o seu chute? "))

if (tentativa > resposta):
    print("Tente um número menor!\n")
elif (tentativa < resposta):
    print("Tente um número maior!\n")
else:
    print("Você acertou!")

