from typing import List
from classes.corrida import Corrida


class Motorista:
    """
    A class to represent a driver.

    Attributes
    ----------
    corridas : List[Corrida]
        A list of rides associated with the driver.
    nota : float
        The rating of the driver.

    Methods
    -------
    __init__(self, corridas: List[Corrida], nota: float):
        Constructs all the necessary attributes for the driver object.
    """

    def __init__(self, corridas: List[Corrida], nota: float):
        self.corridas = corridas
        self.nota = nota
