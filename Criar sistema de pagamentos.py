class FormaDePagamento:
    def processar_pagamento(self):
        print("Processando pagamento de forma genérica.")

class CartaoCredito(FormaDePagamento):
    def processar_pagamento(self):
        print("Pagamento processado com cartão de crédito.")

class PayPal(FormaDePagamento):
    def processar_pagamento(self):
        print("Pagamento processado com PayPal.")

def main():
    print("Escolha uma forma de pagamento:")
    print("1. Cartão de Crédito")
    print("2. PayPal")

    escolha = input("Digite o número correspondente à sua escolha: ")

    if escolha == "1":
        forma_pagamento = CartaoCredito()
    elif escolha == "2":
        forma_pagamento = PayPal()
    else:
        print("Escolha inválida. Encerrando o programa.")
        return


    forma_pagamento.processar_pagamento()

if __name__ == "__main__":
    main()
