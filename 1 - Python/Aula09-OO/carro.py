# Esta classe irá herdar caracteristicas da classe Veiculo
from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Tanque com capacidade inferior a 50 litros")
        else:
            self.tanque += litros