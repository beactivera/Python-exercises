import linecache
import string
#zad1

# text = open('cytaty.txt')
# text.read()
# print(text)
# text.close()

#zad2

# text = open('cytaty.txt','r')
# text.read()
# # text.encode='utf-8'
# print(text)
# # ilosc_wierszy = len(open('cytaty.txt').readlines())
# lines = text.split('\n')
# # print(lines)

# for i in range(len(lines)):
#     if i%2!=0:
#        print(lines[i])
# text.close()

#zad3
# text = open('cytaty.txt','r')
# text.read()
# # text.encode='utf-8'
# # print(text)
# # ilosc_wierszy = len(open('cytaty.txt').readlines())
# lines = text.split('\n')
# # print(lines)

# a = int(input("podaj poczatek zakresu: "))
# b = int(input("podaj koniec zakresu: "))

# for i in range(a-1,b+1):
#     print(lines[i])
# text.close()

#zad4

# lista = []
# nowy_tekst = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst)
# nowy_tekst2 = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst2)
# print(lista)
# plik = open('nowy_plik.txt', 'w')
# plik.writelines(lista)
# plik.close()


#zad5
# lista = []
# nowy_tekst = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst)
# nowy_tekst2 = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst2)
# print(lista)
# plik = open('nieskonczonosc.txt', 'a')
# plik.writelines(lista)
# plik.close()
# plik = open('nieskonczonosc.txt', 'r')
# print(plik.read())
# plik.close()

# #drugi sposob
# lista = []
# nowy_tekst = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst)
# nowy_tekst2 = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst2)
# print(lista)
# plik = open('nieskonczonosc.txt', 'a+')
# plik.writelines(lista)
# plik.seek(0)
# print(plik.read())
# plik.close()


#zad6
# plik = open('nieskonczonosc.txt').read()
# plik = plik.upper()
# print(plik)


#zad7
# plik = open('nieskonczonosc.txt','r').read()
# open('nowy_plik_zad7.txt', 'w').write(plik)


#zad8
# with open('nieskonczonosc.txt') as f: 
#     for line in f: 
#         print(line)
# plik = open('nieskonczonosc.txt','r').read()
# encoding = 'UTF-8'  # polskie znaki - czesc znakow
# words = plik.split(' ')
# print(words)
# dlugosc=0
# slowo=''
# for i in words:
#     if len(i)>dlugosc:
#         dlugosc=len(i)
#         slowo=i
# print(dlugosc, slowo)


#zad9
# text = open('cytaty.txt','r')
# text.read()
# # text.encode='utf-8'
# print(text)
# ilosc_wierszy = len(open('cytaty.txt').readlines())
# print(ilosc_wierszy)


#zad10
# import re

# file = "cytaty.txt"

# with open(file, "r+",encoding="cp1250") as f:
#     data= f.read()
#     data.replace("\n","/")
#     print(data)
#     # data = f.read()
#     # f.seek(0)
#     # f.write(re.sub(r'\n', r'/', data))
#     # f.truncate()
#     # print(data)

#zad11
file = open("zmienne.txt", "r")
zbior=file.read()
words = zbior.split('\n')
print(words)
for elements in words:
    x,y,z=elements.split(" ")
    print(x,y,z)
file.close()

