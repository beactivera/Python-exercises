import string
import random
from random import randrange
import math
#zad1
# for i in range(100):
#     print('*')

#zad2
# for i in range(1,151):
#     print(i)

#zad3
# w=input('wpisz wyraz: ')
# ll = len(w)
# for i in range(0,ll):
#     print(w[i])
#     i+=1

#zad4
# w=input('wpisz wyraz: ')
# ll = len(w)
# for i in range(0,ll):
#    if w[i] in string.punctuation:
#         print(w[i])
#         w=w.replace(w[i],'')
# print(w)

#zad5
# t = (-5, 16, 3.6, 123, -89)
# a=int(input("podaj liczbe: "))
# for i in range (0,len(t)):
#     if t[i]<=a:
#         print(t[i])

#zad6
# for i in range(0,11):
#     a = random.randrange(-2,18)
#     print(a)
#     i+=1

#zad7
# newList = []
# maxTen = []
# for i in range(0,11):
#     a = random.randrange(-2,18)
#     newList.append(a)
#     if a <10:
#         maxTen.append(a)
#
# print(newList)
# print(maxTen)
# lista skladana:
#  x=[random.randint(-2,18) for i in range(10)]

#zad8
# D={}
# x= int(input('podaj liczbe od 1 do 26: '))
# for i in range(97,123):
#         D.setdefault(chr(i),(i-96)**2)
# print(D)
# print(D[chr(x+97)])


#zad9
# w=input('Wpisz lancuch znakow: ')
# ll=len(w)
# D= {}
# for i in range(0,ll):
#     if w[i] in D.keys():
#         D[w[i]] += 1
#     else:
#         D[w[i]]=1
# print(D)

#zad10
# h=input('Podaj haslo:')
#
# for i in range(0,5):
#     if h == 'python':
#         print('poprawne haslo')
#         break
#     else:
#         h=input('zle podane haslo,wprowadz ponownie: ')
#         i+=1

#zad11                     UZUPELNIJ
# for i in range(0,11):
#     if i<6:
#         print('*'*i)
#     else:
#         print('*'*(i-1))

#zad12
# liczby = (4,6,2,43,112,344,234,678,999,44,1,97)
# lp = 0
# lnp = 0
# for i in range(0,len(liczby)):
#     if liczby[i]%2 == 0:
#         lp+=1
#     else:
#         lnp+=1
#
# print('W krotce jest: ', lp , " liczb parzystych i ", lnp, " liczb nieparzystych")

#zad13
# ccz=0
# cdz=0
# for i in range(1,1000):
#     k=pow(i,2)
#     print(k)
#     if k%10 == 4:
#         ccz+=1
#     elif k%10 ==9:
#         cdz+=1
#
# print('ostatnia cyfra 4: ',ccz)
# print('ostatnia cyfra 9: ',cdz)

#zad14               
# tab = [[0 for col in range(10)] for row in range(10)]
# for i in range(1,11,1):
#     for y in range(1,11,1):
#         # if i == 0:
#         #     tab[i][y] = 0
#         # elif y == 0:
#         #     iloczyn = i * y
#         #     tab[-1][1] = iloczyn
#         # else:
#         iloczyn= i * y
#         tab[i-1][y-1] = iloczyn
#     print(tab[i-1])

#zad15
# i=0
# for i in range (100):
#     if i%2 != 0 and i%3 != 0 and i%4 != 0 and i%5 != 0 and i%7 != 0:
#         print(i)
#         i+=1

#zad16
# k=0
# for i in range (100,1000):
#     if i%2 != 0 and i%3 != 0 and i%4 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0 and i%13 != 0 and i%17 != 0 and i%19 != 0:
#         print(i)
#         i+=1
#         k+=1
#
# print('liczb pierwszych w przedziale (100,1000): ',k)

# zad17                        UZUPELNIJ
# tab = [[0 for col in range(5)] for row in range(8)]
# # tab = [[random.randrange(5,10) for col in range(5)] for row in range(8)]
# #print(tab)
# for i in range(8):
#      for y in range(5):
#         tab[i][y] = random.randrange(5,10)
#      print(tab[i])

# zad18
# tab = [[0 for col in range(5)] for row in range(8)]
# counter=0
# for i in range(8):
#      for y in range(5):
#         tab[i][y] = random.randrange(5,10)
#         if tab[i][y]%2 !=0:
#                 counter+=1
# print(tab[i])
# print('Liczb nieparzystych jest: ', counter)

# zad19
# tekst = input("podaj tekst:")
# przes = int(input("podaj przesuniecie: "))
# tekst=list(tekst)
# # print(len(tekst))

# # code in szyfr cezar
# for i in tekst:
#     coded = ord(i) + przes
# # display coded message
#     print(chr(coded), end="")

# tekst1 = input("podaj zakodowany tekst:")
# przes1 = int(input("podaj przesuniecie kodu: "))

# # code in szyfr cezar
# for i in tekst1:
#     coded1 = ord(i) - przes
# # display coded message
#     print(chr(coded1), end="")

# zad20
# for x in range(200):
#     if x%5 == 2 and x%6 == 3 and x%7 == 2:
#         print(x)

# zad21
# dobre=0
# zle=0
# l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(10):
#     a=random.choice(l)
#     b=random.choice(l)
#     print(a, 'razy' , b)
#     odp=int(input("="))
#     if odp == a*b:
#         dobre+=1
#         print('dobra odpowiedz')
#     else:
#         zle+=1
#         print('zle, poprawny to', a*b)
# if(dobre == 10):
#     print('gratulacje!')
# print('dobre odp: ', dobre)
# print('zle odp: ', zle)

#zad22
#FIRST SOLUTION
# # pascals_tri_formula = [] # don't collect in a global variable.
# def combination(n, r): # correct calculation of combinations, n choose k
#     return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

# def for_test(x, y): # don't see where this is being used...
#     for y in range(x):
#         return combination(x, y)

# def pascals_triangle(rows):
#     result = [] # need something to collect our results in
#     # count = 0 # avoidable! better to use a for loop, 
#     # while count <= rows: # can avoid initializing and incrementing 
#     for count in range(rows): # start at 0, up to but not including rows number.
#         # this is really where you went wrong:
#         row = [] # need a row element to collect the row in
#         for element in range(count + 1): 
#             # putting this in a list doesn't do anything.
#             # [pascals_tri_formula.append(combination(count, element))]
#             row.append(combination(count, element))
#         result.append(row)
#         # count += 1 # avoidable
#     return result

def gen(n,r=[]):
    for x in range(n):
        l = len(r)
        r = [1 if i == 0 or i == l else r[i-1]+r[i] for i in range(l+1)]
        yield r

def draw_beautiful(n):
    ps = list(gen(n))
    max = len(' '.join(map(str,ps[-1])))
    for p in ps:
        print(' '.join(map(str,p)).center(max)+'\n')

# now we can print a result:
rows = int(input('Podaj ile wierszy trojkata Pascala: '))
#FIRST SOLUTION
# for row in pascals_triangle(rows):
#      print(row)
draw_beautiful(rows)
