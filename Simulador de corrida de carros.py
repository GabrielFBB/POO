import random


# Definição da classe Carro
class Carro:
    vencedor = ""  # Membro estático para armazenar o nome do carro vencedor

    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade

    def correr(self):
        # Simula o tempo da corrida baseado na velocidade do carro
        tempo = random.uniform(10, 100) / self.velocidade
        return tempo


# Função para rodar a corrida e determinar o vencedor
def realizar_corrida(carros):
    tempos = []

    for carro in carros:
        tempo = carro.correr()
        tempos.append((carro, tempo))

    # Ordena os carros pelo tempo de corrida (menor tempo primeiro)
    tempos.sort(key=lambda x: x[1])

    # O carro com o menor tempo vence
    vencedor = tempos[0][0]

    # Atualiza o membro estático vencedor da classe Carro
    Carro.vencedor = vencedor.nome

    # Exibe o resultado
    print(f'O carro vencedor é: {Carro.vencedor}')
    print(f'O tempo da corrida do vencedor ({vencedor.nome}) foi: {tempos[0][1]:.2f} segundos')


# Função principal para interação com o usuário
def main():
    # Criação de carros
    carro1 = Carro("Ferrari", 350)
    carro2 = Carro("Lamborghini", 340)
    carro3 = Carro("Porsche", 320)

    # Apresentação ao usuário
    print("Escolha seu carro:")
    print("1 - Ferrari (350 km/h)")
    print("2 - Lamborghini (340 km/h)")
    print("3 - Porsche (320 km/h)")

    escolha = int(input("Digite o número do carro escolhido: "))

    # Determinando o carro escolhido
    if escolha == 1:
        carro_escolhido = carro1
    elif escolha == 2:
        carro_escolhido = carro2
    elif escolha == 3:
        carro_escolhido = carro3
    else:
        print("Escolha inválida!")
        return

    print(f"Você escolheu o {carro_escolhido.nome}. Boa sorte na corrida!")

    # Realizando a corrida
    realizar_corrida([carro1, carro2, carro3])


# Executando o programa principal
if __name__ == "__main__":
    main()
