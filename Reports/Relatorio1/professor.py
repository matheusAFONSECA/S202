class Professor:
    """
    Classe que representa um professor.
    Atributos:
        nome (str): O nome do professor.
    Métodos:
        ministrar_aula(self, assunto: str) -> str:
            Retorna uma string informando que o professor está ministrando uma aula sobre o assunto fornecido.
    """
    def __init__(self, nome: str):
        self.nome = nome

    def ministrar_aula(self, assunto: str) -> str:
        """
        Método que simula a ação de um professor ministrando uma aula.
        Parâmetros:
            assunto (str): O assunto da aula.
        Retorna:
            str: Uma string informando que o professor está ministrando uma aula sobre o assunto fornecido.
        """
        
        return f"O professor(a) {self.nome} está ministrando uma aula sobre {assunto}"
