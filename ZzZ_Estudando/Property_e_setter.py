class Pessoa:
    
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

        
    @property                            # Propert usado para retornar um valor
    def nome(self):
        print('Estou no property nome')
        return self._nome
    

    @property                            # Propert usado para retornar um valor
    def idade(self):
        print('Estou no property idade')
        return self._idade


    @nome.setter                          # Setter usado para alterar um valor, não usa return
    def nome(self, valor=None):
        print('Entrei no setter nome')
        self._nome = valor


    @idade.setter                         # Setter usado para alterar um valor, não usa return
    def idade(self, valor=None):
        print('Entrei no setter idade')
        self._idade = valor


################################################################

p1 = Pessoa('Merari', 35)

print(p1.nome)
print(p1.idade)

# auterando a variavel p1. usando o setter
p1.nome = 'Dayvson'
p1.idade = 32

print(p1.nome, p1.idade)
