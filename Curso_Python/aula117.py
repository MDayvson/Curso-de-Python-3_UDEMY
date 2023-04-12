# def duplicar(num):
#     return num * 2


# def triplicar(num):
#     return num * 3


# def quadruplicar(num):
#     return num * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(4))
print(quadruplicar(2))



# Outro exemplo

def saldacao(saldacao):
    def saldar(nome):
        return f'{saldacao}, {nome}!'
    return saldar


dia = saldacao('Bom dia')
tarde = saldacao('Boa tarde')
noite = saldacao('Boa noite')


print(dia('Merari'))
