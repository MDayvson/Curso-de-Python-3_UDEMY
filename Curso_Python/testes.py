def soma(*num):
    s = 0
    for numero in num:
        s += numero
    return s


som = soma(1, 5, 6, 7, 5, 5, 4, 4)


print(f'A soma é {som}')
print(soma(som))
