from dataclasses import dataclass
import abc


class Conta(abc.ABC):
    agencia: int
    conta: int
    saldo: float = 0

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def extrato(self, msg: str = '') -> None:
        print(f'{msg} | O seu saldo é R$ {self.saldo:.2f}')
        print('---')

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.extrato(f'Depositado R$ {valor}')
            return self.saldo


@dataclass
class ContaPoupanca(Conta):
    agencia: int
    conta: int
    saldo: float

    def sacar(self, valor: float) -> float:
        saldo_final = self.saldo - valor
        if saldo_final >= 0:
            self.saldo -= valor
            self.extrato(f'Saque realizado no valor de R$ {valor}')
            return self.saldo
        print(f'Não foi possível realizar o saque no valor de R$ {valor}')
        return self.saldo


@dataclass
class ContaCorrente(Conta):
    agencia: int
    conta: int
    saldo: float
    limite: float = 0

    def sacar(self, valor: float) -> float:
        saldo_final = self.saldo - valor
        limite_maximo = -self.limite

        if saldo_final >= limite_maximo:
            self.saldo -= valor
            self.extrato(f'Saque realizado no valor de R$ {valor}')
            return self.saldo
        print(f'Não foi possivel sacar o valor de R$ {valor}')
        print(f'Seu limite é de {-self.limite}')
        return self.saldo


if __name__ == '__main__':
    cp1 = ContaPoupanca(1580, 13, 100)
    cp1.depositar(5)
    cp1.sacar(50)

    cc1 = ContaCorrente(1580, 21, 0, 1000)
    cc1.depositar(0)
    cc1.sacar(1000)
