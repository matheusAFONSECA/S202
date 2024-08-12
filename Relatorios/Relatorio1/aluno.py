class Aluno:
    """
    Classe que representa um aluno.
    Atributos:
        nome (str): O nome do aluno.
    Métodos:
        presenca() -> str: Retorna uma mensagem informando que o aluno está presente.
    """
    def __init__(self, nome: str):
        self.nome = nome

    def presenca(self):
        """
        Retorna uma mensagem informando que o aluno está presente.
        Retorna:
            str: Mensagem informando que o aluno está presente.
        """
        return f"O aluno(a) {self.nome} está presente"
