class Carro:
    def __init__(self, name):
        self._name = name
        self._motor = None
        self._fabricante = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value


class Motor:
    def __init__(self, name):
        self.name = name


class Fabricante:
    def __init__(self, name):
        self.name = name


################################################################
################################################################
ferrari = Carro('Ferrari')
fiat = Fabricante('Fiat')
motor_5_0 = Motor('5.0')

ferrari.fabricante = fiat
ferrari.motor_5_0 = motor_5_0
print(ferrari.name, ferrari.fabricante.name, ferrari.motor_5_0.name)

################################################################
mercedes = Carro('Mercedes')
bmw = Fabricante('BMW')

mercedes.fabricante = bmw
mercedes.motor_5_0 = motor_5_0
print(mercedes.name, mercedes.fabricante.name, mercedes.motor_5_0.name)
