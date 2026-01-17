import random as r
Pontuação = 0
print("Bem vindo a tabuadeira")
print("A Tabuadeira é um jogo que consiste em acertar a tabuada ")

for i in range(5):
    Primeiro = r.randint(1,9)

    Segundo = Primeiro

    print(Primeiro,"*",Segundo,"=",end="")

    product=Primeiro*Segundo

    ask=eval(input(""))

    if (ask==product):
        Pontuação+=10
        print("Você acertou !")
        print("Pontuação total=" ,Pontuação,"/50")

    else:
         print("Você errou.")

