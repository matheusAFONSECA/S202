from professor import Professor
from aluno import Aluno

class Aula:
    """
    Classe que representa uma aula.
    Atributos:
        professor (Professor): O professor responsável pela aula.
        assunto (str): O assunto da aula.
        alunos (list[Aluno]): A lista de alunos presentes na aula.
    Métodos:
        adicionar_aluno(self, aluno: Aluno):
            Adiciona um aluno à lista de alunos presentes na aula.
        listar_presenca(self) -> str:
            Retorna uma string com a lista de alunos presentes na aula.
    """

    def __init__(self, professor: Professor, assunto: str):
        self.professor = professor
        self.assunto = assunto
        self.alunos = []  # Create an empty list of students

    def adicionar_aluno(self, aluno: Aluno):
        """
        Adiciona um aluno à lista de alunos presentes na aula.
        Parâmetros:
            aluno (Aluno): O aluno a ser adicionado à lista.
        Retorna:
            NONE
        """
        self.alunos.append(aluno)

        return None
    
    def listar_presenca(self) -> str:
        """
        Adiciona um aluno à lista de alunos presentes na aula.
        Retorna:
            str: Uma string com a lista de alunos presentes na aula.
        """
        print(f"Presença(s) na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:")

        return '\n'.join([f"O(a) aluno(a) {aluno.nome} está presente." for aluno in self.alunos])

