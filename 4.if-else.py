#zad2
# l=int(input("podaj liczbe: "))
# if l%2 == 0:
#     print('To jest liczba parzysta')
# else:
#     print('To jest liczba nieparzysta')

#zad3
# lit=input("podaj litere: ")
# l=list('bardzodlugiwyraz')
# a="".join(l)
# # print(a)
# if a.find(lit)== -1:
#     print('litera jest na liscie')
# else:
#     print('litera nie jest na liscie')

#zad4
# x1=int(input('Podaj pierwsza liczbe: '))
# x2=int(input('Podaj druga liczbe: '))
# x3=int(input('Podaj trzecia liczbe: '))
# if x1==x2==x3:
#     print((x1+x2+x3)**2)
# else:
#     print(x1+x2+x3)

#zad5
# x1=int(input('Podaj pierwsza liczbe: '))
# x2=int(input('Podaj druga liczbe: '))
# suma=x1+x2
# if suma>15 and suma<=20:
#     print(20)
# else:
#     print(suma)

#zad6
# x1=float(input('Podaj pierwsza liczbe: '))
# x2=float(input('Podaj druga liczbe: '))
# if x1%1 == 0 and x2%1 == 0:
#     suma=x1+x2
#     print(suma)
# else:
#     print('ktoras liczba nie jest calkowita')

#zad7
# D = {'a':1,'aa':2,'abc':32,'nowy':66,'xyz':'ijk'}
# x=str(input('podaj element: '))
# print(x)
# print(D.keys())
# if x in D.keys():
#     print('tak: ', D.get(x))
# else:
#     y=input('podaj wartosc: ')
#     D.setdefault( x, y)
#     print(D)

#zad8
# x=input('wprowadz lancuch znbakow: ')
# print(x[0])
# l=len(x)
# print(l)
# if l>=0 and l<4:
#     print('za krotki lancuch')
# else:
#     suma=x[0:2]+x[l-2:l]
#     print(suma)

#zad9
zdanie=input('wprowadz zdanie: ')
wyrazy=zdanie.split(" ")
# wyrazy = tuple(wyrazy)
print(wyrazy)
if 'nic' in wyrazy:
    ix=wyrazy.index('nic')
    print(wyrazy.index('nic'))
else:
    break




