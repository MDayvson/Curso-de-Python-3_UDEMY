# replicando aula de decoradores de classes e metodos


def meu_repr(self,):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}, ({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def melhor_time(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Flamengo' in resultado:
            return 'Realmente o Flamengo é melhor'
        return resultado
    return interno


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Voçê está em casa'
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

    @melhor_time
    def melhor(self):
        return f'O time é {self.nome}'


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


flamengo = Time('Flamengo')
real = Time('Real Madri')
terra = Planeta('Terra')
jupter = Planeta('Jupter')

print(flamengo)
print(real)

print(terra)
print(jupter)


print(flamengo.melhor())
print(real.melhor())

print(terra.falar_nome())
print(jupter.falar_nome())
