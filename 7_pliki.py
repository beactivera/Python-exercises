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

#drugi sposob
lista = []
nowy_tekst = input("podaj tekst do wpisania: ")
lista.append(nowy_tekst)
nowy_tekst2 = input("podaj tekst do wpisania: ")
lista.append(nowy_tekst2)
print(lista)
plik = open('nieskonczonosc.txt', 'a+')
plik.writelines(lista)
plik.seek(0)
print(plik.read())
plik.close()



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
# for i in words:
#     if words[i]>words[i+1]:
#         print(words[i],len(words[i]))
#     else:
#         print(words[i+1],len(words[i+1]))


# Python
# def longest_words(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]

# print(longest_words('about.txt'))
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# def longest_words(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]
 
# print(longest_words('about.txt'))
# # szukam=find(tekst,'ala ma kota')
# # if szukam>-1:
# #    print "znalazlem"
# # else:
# #    print "nie znalazlem."


