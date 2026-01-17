
def coletar_dados():
    nome = input("Digite o nome do estudante: ")
    idade = int(input("Digite a idade do estudante: "))
    nota = float(input("Digite a nota do estudante no exame: "))

    estudante = {"Nome": nome,"Idade": idade, "Nota": nota}

    return estudante


def exibir_dados(estudante):
    print("\nInformações do Estudante:")
    print(f"Nome: {estudante['Nome']}")
    print(f"Idade: {estudante['Idade']} anos")
    print(f"Nota no Exame: {estudante['Nota']:.2f}")



def main():
    estudante = coletar_dados()
    exibir_dados(estudante)

if __name__ == "__main__":
    main()
