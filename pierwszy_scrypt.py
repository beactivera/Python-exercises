import math
import sys
import random
import string
#lista 3 zad1
'''
print('W dzien zwykly i od swieta:','\n','\t','nie dziel przez 0,','\n\t\tPAMIETAJ!')
'''
#zad2
"""
i=input('Wpisz imie: ')
n=input('Wpisz nazwisko: ')
print(i,' ',n,'!')
"""
#zad3
'''
r=float(input('podaj promien kola: '))
p= math.pi*r**2
l=2*math.pi*r
print('pole kola wynosi: ',p,'obwod kola wynosi: ',l)
'''
#zad4
'''
t=float(input('podaj punkt: '))
#kiedy stosujemy dana biblioteke i jej elementy musimy przy kazdym uzyciu podac nazwe_biblio.element
wartosc_koncowa=t**2+t**4-2*math.sin(t/2)+math.exp(t+2)
print(wartosc_koncowa)
'''
#zad5
'''
print(sys.version)
'''
#zad6
'''
rand=input('wpisz ciag znakow: ')
lista =rand.split(sep=" ")
krotka=tuple(lista)
print(lista, krotka)
'''
#zad7
'''
i=input('Wpisz imie: ')
w=int(input('Wpisz wiek: '))
rok=2019-w
print(i,' ma ',w,' lat ', ', to znaczy, ze urodzil sie w ',rok,' roku')
'''
#zad8
'''
napis='Matematyka jest super!\n'
print(napis*50)
'''
#zad9
'''
x=int(input("Wpisz stopnie celcjusza: "))
fs=str(32+(9/5)*x)
print('Jest równe ' + fs + ' stopni w skali Fahrenheita')
'''
#zad10
'''
x=int(input("Podaj wage: "))
funty=round(x*2.20462262)
print('Jest to ', funty, 'funtów')
'''
#zad11
'''
l=list('kalambur')
print(l)
random.shuffle(l)
print(l)
s=""
print(s.join(l))
'''
#zad12
'''
a=int(input('Podaj x1: '))
b=int(input('Podaj y1: '))
c=int(input('Podaj x2: '))
d=int(input('Podaj y2: '))
odl=math.sqrt((a-c)**2+(b-d)**2)
print('Odleglosc miedzy tymi punktami: ',odl)
'''
#zad13
'''
s=int(input('Podaj ilosc sekund: '))
dni = int(s/86400)
godzin = int(s/3600)
minut= int(s/60)
sekund =s
print('Dni: ', dni)
print('Godzin: ', godzin)
print('Minut: ', minut)
print('Sekund: ', sekund)
'''
#zad14
'''
wag=int(input('Podaj swoja wage: '))
wzr=int(input('Podaj swoj wzrost: '))
bmi=wag/(wzr**2)
print('Twoje BMI wynosi: ', bmi)
'''
#zad15
'''
rach=int(input('Podaj kwote rachunku: '))
tip=int(input('Podaj procent napiwku: '))
ntip=(tip/100)*rach
print('Masz do zaplaty: ', rach+ntip)
'''
#zad16
'''
napis= input('podaj ciag znakow: ')
napis =napis.replace("a","&")
print(napis)
'''
#zad17
'''
napis= input('podaj ciag znakow: ')
napis =napis.replace("a","")
print(napis)
'''
#zad18
# zdanie = str(input('Podaj zdanie: '))
# zdanie = zdanie.title()
# wyrazy=zdanie.split(" ")
# wyrazy.sort()
# wyrazy = tuple(wyrazy)
# print(" ".join(wyrazy))


#zad19
# kat=int(input('Podaj kat: '))
# s=math.sin(kat)
# print("%.2f" %s)

#zad20
n=int(input('Podaj n: '))
l=3**n
o=l%10
print(o)
