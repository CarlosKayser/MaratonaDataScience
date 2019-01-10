"""
EXERCICIO:

Crie um software de gerenciamento bancário
- Esse software deverá ser capaz de cadastrar clientes e contas
- Cada cliente possui nome, idade, cpf
- Cada conta possui um cliente, saldo, limite com os métodos sacar, depositar e consultar saldo 
"""

from Cliente import Cliente
from Conta import Conta

cliente = Cliente('Carlos', '000.000.000-00', 20)

print(cliente)

conta_carlos = Conta(cliente, 20, 100)

print("Saldo:",conta_carlos.consultar_saldo())

conta_carlos.depositar(1000)

print("Saldo:",conta_carlos.consultar_saldo())

conta_carlos.sacar(100)

print("Saldo:",conta_carlos.consultar_saldo())

conta_carlos.sacar(1000)

print("Saldo:",conta_carlos.consultar_saldo())
