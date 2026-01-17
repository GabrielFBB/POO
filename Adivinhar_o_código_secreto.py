import random

numero = random.randint(1,100)

tentativas = 0

if tentativas == 10:
    print("Estorou o numero de tentativas.Tente de novo se quiser")

print("Bem vindo ao jogo de adivinhação !!!")
print("Será que você será o grande vencedor ? Tente sua sorte. ")

while True:
    tentativas = tentativas + 1
    tentativa = int(input("Dê o seu palpite:"))

    if numero == tentativa:
        print("Bravoo !!! Meus parabéns você acertou.")
        break
    else:
        if numero < tentativa:
            print("O número é menor que a sua tentativa")
        if numero > tentativa:
            print("O número é maior que a sua tentativa")


