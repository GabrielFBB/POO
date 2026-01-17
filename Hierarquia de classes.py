
class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitirSom(self):
        print("O animal emite um som.")

class Cão(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f"O {self._nome} está latindo.")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print(f"O {self._nome} está miando.")


def main():

    nome_cão = input("Digite o nome do cão: ")
    cão = Cão(nome_cão)
    cão.emitirSom()
    cão.latir()

    nome_gato = input("Digite o nome do gato: ")
    gato = Gato(nome_gato)
    gato.emitirSom()
    gato.miar()


if __name__ == "__main__":
    main()
