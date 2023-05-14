
from dataclasses import dataclass
from abc import ABC


class conta(ABC):
    ...


@dataclass
class ContaPoupanca:
    agencia: int
    conta: int
    saldo: float

    def extrato(self, msg):
        print(f'{self.saldo}')

    def sacar(self, saque):
        if self.saldo >= 0:
            self.saldo -= saque
        return self.saldo


if __name__ == '__main__':
    cp1 = ContaPoupanca(1580, 31, 100)

    cp1.sacar(5)
