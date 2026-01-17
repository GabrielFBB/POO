print("Bem vindo a calculadora da Área do Triângulo.")

a = float(input(">Insira o tamanho do 1ºlado do triângulo. "))
b = float(input(">Insira o tamanho do 2ºlado do triângulo. "))
c = float(input(">Insira o tamanho do 3ºlado do triângulo. "))

s = (a + b + c)/2

área = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("\nÁrea do triângulo é",área )

if a == b == c:
    print("> É um triângulo equilátero")

elif (a != b) and (b != c) and (c != a):
    print("> É um triângulo escaleno")

elif a == b and b != c or c == a and b != a:
    print("> É um triângulo isósceles")
