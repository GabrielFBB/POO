class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo=0.0):
        self.__numero_conta = numero_conta
        self.__nome_titular = nome_titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def levantar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Levantamento de {valor} realizado com sucesso.")
        else:
            print("Valor de levantamento inválido ou saldo insuficiente.")

    def verificar_saldo(self):
        print(f"Saldo atual: {self.__saldo}")

    @property
    def nome_titular(self):
        return self.__nome_titular

    @nome_titular.setter
    def nome_titular(self, nome):
        if nome:
            self.__nome_titular = nome
        else:
            print("Nome inválido.")

if __name__ == "__main__":
    print("Bem-vindo ao sistema bancário!")

    numero = int(input("Digite o número da conta: "))
    titular = input("Digite o nome do titular: ")

    conta = ContaBancaria(numero, titular)

    while True:
        print("\nEscolha uma operação:")
        print("1. Verificar saldo")
        print("2. Depositar")
        print("3. Levantar")
        print("4. Alterar nome do titular")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == "1":
            conta.verificar_saldo()
        elif escolha == "2":
            valor = float(input("Digite o valor para depósito: "))
            conta.depositar(valor)
        elif escolha == "3":
            valor = float(input("Digite o valor para levantamento: "))
            conta.levantar(valor)
        elif escolha == "4":
            novo_nome = input("Digite o novo nome do titular: ")
            conta.nome_titular = novo_nome
            print(f"Nome do titular atualizado para: {conta.nome_titular}")
        elif escolha == "5":
            print("Obrigado por utilizar o sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
