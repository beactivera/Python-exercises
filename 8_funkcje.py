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
# def porownanie(lista1, lista2):
#     return(bool(lista1 in lista2))

# lista1 = [random.randrange(-50,101) for i in range(10)]
# lista2 = [-2*7**2-10*t+111 for t in range(17)]

# print(lista1)
# print(lista2)

# wynik = porownanie(lista1, lista2)
# print(wynik)

#zad6
# def tworzenie_slownika(wyraz):
#     slownik = {}
#     dlug = len(wyraz)
#     for i in range(0,dlug):
#         if wyraz[i] in slownik.keys():
#             slownik[wyraz[i]] += 1
#         else:
#             slownik[wyraz[i]]=1
#     return slownik

# def laczenie_slownika(wyraz1, wyraz2):
#     slownik = {}
#     dlug1 = len(wyraz1)
#     for i in range(0,dlug1):
#         if wyraz1[i] in slownik.keys():
#             slownik[wyraz1[i]] += 1
#         else:
#             slownik[wyraz1[i]]=1
#     dlug2 = len(wyraz2)
#     for i in range(0,dlug2):
#         if wyraz2[i] in slownik.keys():
#             slownik[wyraz2[i]] += 1
#         else:
#             slownik[wyraz2[i]]=1
#     return slownik
   

# jeden = input("podaj pierwszy wyraz: ")
# dwa = input("podaj drugi wyraz: ")

# wspolny = {}

# koncowy = laczenie_slownika(jeden, dwa)
# print(koncowy)

#zad7
# def funkcja(n):
#     if n==1:
#         return 1
#     else: 
#         for k in range(math.ceil(math.sqrt(n))+1):
#             if math.pow(k,2)<=n and math.pow(k+1,2)>n:
#                 return k

# lista = []
        
# for k in range(10):
#     n = random.randint(1,101)
#     print(n)

#     while n>=1:    
#         liczba = funkcja(n)
#         print(liczba,sep='',end=' ')
#         n=n-(math.pow(liczba,2))

#     print()

#zad8
# def czy_pierwsza(n):

#     for x in range(2, n//2):
#         if n % x == 0:
#             return False
    
#     return True

# lista_poczatkowa = [x for x in range(100, 500)]
# lista_koncowa = [x for x in lista_poczatkowa if not czy_pierwsza(x)]

# print(lista_koncowa)

#zad9

# import func as f

# x = int(input('Podaj 1 liczbe: '))
# y = int(input('Podaj 2 liczbe: '))

# print(f.stworz_liste(x))
# print(f.stworz_liste(y))
# print(f.stworz_liste(2*x, y))

#zad10

# def suma_dzielnikow(liczba):

#     dzielniki = []

#     for x in range(1, liczba):
#         if liczba % x == 0:
#             dzielniki.append(x)

#     return sum(dzielniki)

# for x in range(1, 10001):

#     if suma_dzielnikow(x) == x:
#         print(x)

# zad 11

# def silnia(liczba):

#     a = 1

#     for x in range(1, liczba + 1):
#         a = a * x

#     return a

# def suma_szeregu(k):

#     elementy_szeregu = []

#     for x in range(k+1):
#         elementy_szeregu.append(1/(silnia(k)))

#     return sum(elementy_szeregu)

# print(suma_szeregu(100))
# print(suma_szeregu(1000))
# print(suma_szeregu(10000))

# zad12

# from time import time

# def silnia(liczba):

#     a = 1

#     for x in range(1, liczba + 1):
#         a = a * x

#     return a

# def silnia_rekurencja(liczba):

#     if liczba == 1 or liczba == 0:
#         return 1
#     else:
#         return liczba * silnia_rekurencja(liczba - 1)

# def suma_szeregu(k, funkcja_silni):

#     elementy_szeregu = []

#     for x in range(k+1):
#         elementy_szeregu.append(1/(funkcja_silni(k)))

#     return sum(elementy_szeregu)


# print('Test - iteracyjna funkcja silni')

# start = time()

# print(suma_szeregu(100, silnia))
# print(suma_szeregu(400, silnia))
# print(suma_szeregu(800, silnia))

# koniec = time()

# print('Wynik:', round(koniec-start, 2), 's')

# print('Test - rekurencyjna funkcja silni')

# start = time()

# print(suma_szeregu(100, silnia_rekurencja))
# print(suma_szeregu(400, silnia_rekurencja))
# print(suma_szeregu(800, silnia_rekurencja))


# koniec = time()

# print('Wynik:', round(koniec-start, 2), 's')

# zad13

# def fibo(n):

#     a = 1
#     b = 1

#     zwracana = 1 

#     for x in range(n):

#         zwracana = a

#         suma_a_b = a + b
#         a = b 
#         b = suma_a_b 
        
#     return zwracana


# def element_ciag_1(n):

#     return fibo(n) - (1/math.sqrt(5)) * ((1 + math.sqrt(5))/2)**n

# def element_ciag_2(n):

#     return ((fibo(n+1)/fibo(n)) - (1+math.sqrt(5))/2)

# def wyswietl_k_elementow_ciagu(n, ciag):

#     print([ciag(x) for x in range(n)])

# wyswietl_k_elementow_ciagu(10, element_ciag_1)
# wyswietl_k_elementow_ciagu(10, element_ciag_2)

# zad14

# def suma_cyfr_w_liczbie(n):

#     pierwsza = n % 10
#     druga = n // 10

#     return pierwsza + druga


# def stworz_slownik():

#     slownik = {}

#     for x in range(1, 101):
#         if suma_cyfr_w_liczbie(x) in slownik.keys():
#             slownik[suma_cyfr_w_liczbie(x)] += 1
#         else:
#             slownik[suma_cyfr_w_liczbie(x)] = 1

#     print(slownik)

# stworz_slownik()

# zad16

def zwroc_maciez_zerowa(n, k = -1):

    if k == -1:
        k = n

    macierz = []

    for wiersz in range(k):

        w = []

        for kolumna in range(n):

            w.append(0)

        macierz.append(w)
    
    return macierz


def wypisz_macierz(m):

    for w in m:
        for k in w:
            print(k, end=' ')
        print()


def zwroc_maciez_identycznosciowa(n):

    tmp_macierz = zwroc_maciez_zerowa(n, n)

    for x in range(len(tmp_macierz)):
        for y in range(len(tmp_macierz[0])):
            if x == y:
                tmp_macierz[x][y] = 1

    return tmp_macierz


def zwroc_iloczyn_macierzy(m_1, m_2):
    pass

m_1 = zwroc_maciez_zerowa(3)
wypisz_macierz(m_1)

print()

m_2 = zwroc_maciez_identycznosciowa(4)
wypisz_macierz(m_2)


# mnozenie macierzy

http://enroute.pl/obliczenia-na-macierzach-numpy/

# wczytywanie z pliku txt  






