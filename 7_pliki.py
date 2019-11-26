import linecache
#zad1

# text = open('cytaty.txt').read()
# print(text)

#zad2

# text = open('cytaty.txt','r').read()
# # text.encode='utf-8'
# print(text)
# # ilosc_wierszy = len(open('cytaty.txt').readlines())
# lines = text.split('\n')
# # print(lines)

# for i in range(len(lines)):
#     if i%2!=0:
#        print(lines[i])

#zad3
# text = open('cytaty.txt','r').read()
# # text.encode='utf-8'
# # print(text)
# # ilosc_wierszy = len(open('cytaty.txt').readlines())
# lines = text.split('\n')
# # print(lines)

# a = int(input("podaj poczatek zakresu: "))
# b = int(input("podaj koniec zakresu: "))

# for i in range(a-1,b+1):
#     print(lines[i])

#zad4

# lista = []
# nowy_tekst = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst)
# nowy_tekst2 = input("podaj tekst do wpisania: ")
# lista.append(nowy_tekst2)
# print(lista)
# open('nowy_plik.txt', 'w').writelines(lista)


#zad5
lista = []
nowy_tekst = input("podaj tekst do wpisania: ")
lista.append(nowy_tekst)
nowy_tekst2 = input("podaj tekst do wpisania: ")
lista.append(nowy_tekst2)
print(lista)
plik = open('nieskonczonosc.txt', 'a')
plik.writelines(lista)
plik.close()


