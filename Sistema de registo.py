class Aluno:

    NúmeroEstudantes = 0

    def __init__(self,nome,idade,curso,matrícula):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matrícula = matrícula
        Aluno.NúmeroEstudantes += 1

Estudante1 = Aluno("Renato","17","Python","1212")
Estudante2 = Aluno("Roberto","18","Optometria","2323")

def AlunoInfo(Estudante):
    print(Estudante.nome)
    print(Estudante.idade)
    print(Estudante.curso)
    print(Estudante.matrícula)

@staticmethod
def adicionarEstudante():

    print("Adicionou um Estudante")

AlunoInfo(Estudante1)

AlunoInfo(Estudante2)

print(Aluno.NúmeroEstudantes)



