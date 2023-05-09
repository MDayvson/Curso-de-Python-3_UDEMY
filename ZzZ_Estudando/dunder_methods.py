class Test:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name} x= {self.x!r}, y= {self.y!r}'

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Test(novo_x, novo_y)


teste1 = Test(5, 6)
teste2 = Test(1, 3)

soma = teste1 + teste2

print(soma)
