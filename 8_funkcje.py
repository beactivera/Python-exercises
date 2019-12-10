import math
import random
#zad1
# def f(x):
#     if x>=-1:
#         x=x**2+6*x-2
#         return x
#     else:
#         x=(5*x-3)/(x**2-1)
#         return x


# a=int(input('Podaj liczbe: '))
# b=a+3
# c=-1*a
# wynik = f(a)-3*f(b)+f(c)
# print(wynik)

#zad2
def suma(lista):
    suma = 0
    for i in range(6):
        for j in range(9):
            suma+= lista[i][j]
    return suma

def iloczyn(lista):
    iloczyn = 1
    for i in range(6):
        for j in range(9):
            iloczyn*= lista[i][j]
    return iloczyn

lista = [[random.randrange(10,100) for col in range(9)] for row in range(6)]
print(lista)

print(suma(lista))
print(iloczyn(lista))