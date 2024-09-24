from typing import List
from classes.corrida import Corrida

class Motorista:
    def __init__(self, corridas: List[Corrida], nota: float):
        self.corridas = corridas
        self.nota = nota
