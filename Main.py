class Main:
    pass

from Cliente import Cliente
from Conta import Conta

# Criando um cliente
c1 = Cliente("João", "114444-2222")

# Criando uma conta para o cliente
conta = Conta(c1.get_nome(), 1222, 0)

conta.deposito(100)
conta.saque(50)
conta.extrato()

