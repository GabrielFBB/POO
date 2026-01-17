
class Veiculo:
    def __init__(self, marca, ano):
        self._marca = marca
        self._ano = ano

    def apresentar(self):
        print(f"Marca: {self._marca}")
        print(f"Ano de Fabricação: {self._ano}")



class Carro(Veiculo):
    def __init__(self, marca, ano, num_portas):
        super().__init__(marca, ano)
        self._num_portas = num_portas

    def apresentar(self):
        super().apresentar()
        print(f"Número de portas: {self._num_portas}")



class Moto(Veiculo):
    def __init__(self, marca, ano, tipo):
        super().__init__(marca, ano)
        self._tipo = tipo

    def apresentar(self):
        super().apresentar()
        print(f"Tipo de Moto: {self._tipo}")



def main():
    print("Criação de veículos:")


    marca_carro = input("Digite a marca do carro: ")
    ano_carro = int(input("Digite o ano de fabricação do carro: "))
    num_portas = int(input("Digite o número de portas do carro: "))

    carro = Carro(marca_carro, ano_carro, num_portas)
    print("\nInformações do Carro:")
    carro.apresentar()


    marca_moto = input("\nDigite a marca da moto: ")
    ano_moto = int(input("Digite o ano de fabricação da moto: "))
    tipo_moto = input("Digite o tipo da moto: ")

    moto = Moto(marca_moto, ano_moto, tipo_moto)
    print("\nInformações da Moto:")
    moto.apresentar()



if __name__ == "__main__":
    main()
