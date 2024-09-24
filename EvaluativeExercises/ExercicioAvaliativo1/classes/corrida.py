from classes.passageiro import Passageiro


class Corrida:
    """
    A class to represent a ride.

    Attributes
    ----------
    nota : float
        The rating of the ride.
    distancia : float
        The distance of the ride in kilometers.
    valor : float
        The cost of the ride.
    passageiro : Passageiro
        The passenger of the ride.

    Methods
    -------
    __init__(self, nota: float, distancia: float, valor: float, passageiro: Passageiro):
        Constructs all the necessary attributes for the Corrida object.
    """

    def __init__(
        self, nota: float, distancia: float, valor: float, passageiro: Passageiro
    ):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro
