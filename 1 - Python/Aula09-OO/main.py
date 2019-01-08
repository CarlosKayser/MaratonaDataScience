"""
Aula 9 - Orientação a objeto

"""

from veiculo import Veiculo # Importando somente a classe
from carro import Carro

veiculo1 = Veiculo('Azul', 4, 'Fiat', 50)

print("")
print(type(veiculo1))
print("Fiat")
print('Cor:', veiculo1.cor)
print('Marca:', veiculo1.marca)
print('Tanque:', veiculo1.tanque)

veiculo2 = Carro('Preto', 'BMW', 30)

print("")
print(type(veiculo2))
print("BMW")
print('Cor:', veiculo2.cor)
print('Marca:', veiculo2.marca)
print('Tanque:', veiculo2.tanque)
veiculo2.abastecer(30)
print('Tanque:', veiculo2.tanque)
veiculo2.abastecer(30)
print('Tanque:', veiculo2.tanque)
