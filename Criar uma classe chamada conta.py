class Conta:
    def __init__(self, titular, numero_conta, quantidade):
        self.titular = titular
        self.numero_conta = numero_conta
        self.quantidade = quantidade

    def __str__(self):
        return f"Conta de {self.titular} (Número: {self.numero_conta}) com saldo de {self.quantidade} unidades."


conta1 = Conta("Renato", "123123", 500)
conta2 = Conta("Roberto", "321321", 300)


if conta1.quantidade > conta2.quantidade:
    print(f"{conta1.titular} tem mais dinheiro que {conta2.titular}.")
elif conta1.quantidade < conta2.quantidade:
    print(f"{conta2.titular} tem mais dinheiro que {conta1.titular}.")
else:
    print(f"{conta1.titular} e {conta2.titular} têm a mesma quantidade de dinheiro.")
