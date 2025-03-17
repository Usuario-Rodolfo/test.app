class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta

# Criando um cliente
c1 = Cliente("João", "114444-2222")

# Criando uma conta associada ao cliente
conta = Conta(c1.nome, 6565, 0)

# Exibindo os detalhes da conta
print(f"{conta.titular} - Número: {conta.numero} - Seu Saldo: {conta.saldo}")