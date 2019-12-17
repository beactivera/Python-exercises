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
# def suma(lista):
#     suma = 0
#     for i in range(6):
#         for j in range(9):
#             suma+= lista[i][j]
#     return suma

# def iloczyn(lista):
#     iloczyn = 1
#     for i in range(6):
#         for j in range(9):
#             iloczyn*= lista[i][j]
#     return iloczyn

# lista = [[random.randrange(10,100) for col in range(9)] for row in range(6)]
# print(lista)

# print(suma(lista))
# print(iloczyn(lista))


#zad3
# def max_z_listy(lista):
#     return max(lista)

# lista = []
# n = int(input('Podaj ile elementow w liscie: '))

# for i in range(n):
#     lista.append(math.sin(i))
# # print(lista)

# maxlist = max_z_listy(lista)
# print(maxlist)


#zad4
# def usuwanie(znaki):
#     vowel = ["a","e","o","i"]
#     for i in znaki:
#         if i in vowel:
#             znaki = znaki.replace(i," ")
#     return znaki

# lancuch = input("Podaj lancuch znakow: ")

# nowy_lancuch = usuwanie(lancuch)
# print(nowy_lancuch)


#zad5
def porownanie(lista1, lista2):
    return(bool(lista1 in lista2))

lista1 = [random.randrange(-50,101) for i in range(10)]
lista2 = [-2*7**2-10*t+111 for t in range(17)]

print(lista1)
print(lista2)

wynik = porownanie(lista1, lista2)
print(wynik)