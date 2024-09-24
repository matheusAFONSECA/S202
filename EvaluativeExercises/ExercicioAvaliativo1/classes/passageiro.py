class Passageiro:
    """
    A class used to represent a Passenger.
    Attributes
    ----------
    nome : str
        The name of the passenger.
    documento : str
        The document identifier of the passenger.
    Methods
    -------
    dict():
        Returns a dictionary representation of the passenger.
    """

    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def dict(self):
        return {"nome": self.nome, "documento": self.documento}
