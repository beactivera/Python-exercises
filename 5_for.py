import string
import random
from random import randrange
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

#zad8               UZUPELNIJ


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

# zad17
tab = [[0 for col in range(5)] for row in range(8)]
for i in range(5):
     for y in range(8):
        tab[i][y] = randrange(5,9)
print(tab[i])


