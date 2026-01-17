from abc import ABC, abstractmethod

class Lutador(ABC):
    @abstractmethod
    def atacar(self, oponente):
        pass

    @abstractmethod
    def defender(self, dano):
        pass

    @abstractmethod
    def obter_vida(self):
        pass

class HomemDeFerro(Lutador):
    def __init__(self):
        self.__vida = 200

    def atacar(self, oponente):
        dano = 25
        print("Homem de Ferro ataca com seus repulsores!")
        oponente.defender(dano)

    def defender(self, dano):
        dano_reduzido = max(dano - 12, 0)
        self.__vida -= dano_reduzido
        print(f"Homem de Ferro defende e reduz o dano para {dano_reduzido}.")

    def obter_vida(self):
        return self.__vida

class FeiticeiraEscarlate(Lutador):
    def __init__(self):
        self.__vida = 180

    def atacar(self, oponente):
        dano = 28
        print("Feiticeira Escarlate ataca com magia do caos!")
        oponente.defender(dano)

    def defender(self, dano):
        dano_reduzido = max(dano - 10, 0)
        self.__vida -= dano_reduzido
        print(f"Feiticeira Escarlate defende e reduz o dano para {dano_reduzido}.")

    def obter_vida(self):
        return self.__vida

class Thor(Lutador):
    def __init__(self):
        self.__vida = 220

    def atacar(self, oponente):
        dano = 30
        print("Thor ataca com seu martelo Mjolnir!")
        oponente.defender(dano)

    def defender(self, dano):
        dano_reduzido = max(dano - 15, 0)
        self.__vida -= dano_reduzido
        print(f"Thor defende e reduz o dano para {dano_reduzido}.")

    def obter_vida(self):
        return self.__vida

class Thanos(Lutador):
    def __init__(self):
        self.__vida = 300

    def atacar(self, oponente):
        dano = 35
        print("Thanos ataca com o poder das Joias do Infinito!")
        oponente.defender(dano)

    def defender(self, dano):
        dano_reduzido = max(dano - 18, 0)
        self.__vida -= dano_reduzido
        print(f"Thanos defende e reduz o dano para {dano_reduzido}.")

    def obter_vida(self):
        return self.__vida

class DrDoom(Lutador):
    def __init__(self):
        self.__vida = 190

    def atacar(self, oponente):
        dano = 27
        print("Dr. Doom ataca com feitiços místicos e tecnologia avançada!")
        oponente.defender(dano)

    def defender(self, dano):
        dano_reduzido = max(dano - 12, 0)
        self.__vida -= dano_reduzido
        print(f"Dr. Doom defende e reduz o dano para {dano_reduzido}.")

    def obter_vida(self):
        return self.__vida

class Galactus(Lutador):
    def __init__(self):
        self.__vida = 400

    def atacar(self, oponente):
        dano = 40
        print("Galactus ataca com um poder cósmico devastador!")
        oponente.defender(dano)

    def defender(self, dano):
        dano_reduzido = max(dano - 20, 0)
        self.__vida -= dano_reduzido
        print(f"Galactus defende e reduz o dano para {dano_reduzido}.")

    def obter_vida(self):
        return self.__vida

def batalha():
    print("Escolha dois lutadores para a batalha:")
    print("1. Homem de Ferro")
    print("2. Feiticeira Escarlate")
    print("3. Thor")
    print("4. Thanos")
    print("5. Dr. Doom")
    print("6. Galactus")

    escolha1 = input("Escolha o primeiro lutador (1-6): ")
    escolha2 = input("Escolha o segundo lutador (1-6): ")

    lutadores = {
        "1": HomemDeFerro,
        "2": FeiticeiraEscarlate,
        "3": Thor,
        "4": Thanos,
        "5": DrDoom,
        "6": Galactus
    }

    if escolha1 not in lutadores or escolha2 not in lutadores:
        print("Escolha inválida. Encerrando o programa.")
        return

    lutador1 = lutadores[escolha1]()
    lutador2 = lutadores[escolha2]()

    rodada = 1
    while lutador1.obter_vida() > 0 and lutador2.obter_vida() > 0:
        print(f"\n--- Rodada {rodada} ---")
        print(f"Lutador 1: {lutador1.__class__.__name__} com {lutador1.obter_vida()} de vida.")
        print(f"Lutador 2: {lutador2.__class__.__name__} com {lutador2.obter_vida()} de vida.")

        acao1 = input(f"Lutador 1 ({lutador1.__class__.__name__}), escolha sua ação (atacar/defender): ").strip().lower()
        acao2 = input(f"Lutador 2 ({lutador2.__class__.__name__}), escolha sua ação (atacar/defender): ").strip().lower()

        if acao1 == "atacar":
            lutador1.atacar(lutador2)
        elif acao1 != "defender":
            print("Ação inválida para o Lutador 1.")

        if acao2 == "atacar":
            lutador2.atacar(lutador1)
        elif acao2 != "defender":
            print("Ação inválida para o Lutador 2.")

        rodada += 1

    print("\n--- Resultado Final ---")
    print(f"Lutador 1 ({lutador1.__class__.__name__}) terminou com {lutador1.obter_vida()} de vida.")
    print(f"Lutador 2 ({lutador2.__class__.__name__}) terminou com {lutador2.obter_vida()} de vida.")

    if lutador1.obter_vida() > 0:
        print(f"{lutador1.__class__.__name__} é o vencedor!")
    elif lutador2.obter_vida() > 0:
        print(f"{lutador2.__class__.__name__} é o vencedor!")
    else:
        print("A luta terminou em empate!")

if __name__ == "__main__":
    batalha()
