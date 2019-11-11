#petle

#zad3
# n = int(input('podaj poczatkowa liczbe zakresu: '))
# m = int(input('podaj koncowa liczbe zakresu: '))
# #przedzial rosnacy
# # for i in range(n,m+1):
# #     print(i)
# #przedzial malejacy
# # for i in range(n, m-1, -1):
# #     print(i)
# #przedzial uniwersalny
# if n<m:
#     for i in range(n,m+1):
#         print(i)
# else:
#     for i in range(n, m-1, -1):
#          print(i)

#zad4
# suma=0
# for i in range(0,101):
#     suma += i
# print(suma)

#zad5
# suma=0
# wynik=0
# while wynik<1000000:
#     suma+= 1
#     wynik+=suma
# print(suma-1)

#zad6
# n=0
# wynik=0
# while wynik<10:
#     n+= 1
#     wynik+=float(1)/n
# print(n)

#zad7
# n = int(input('Podaj liczbe: '))
# i=0
# while i<n:
#     i+=1
#     if i**2==n:
#         print('podana liczba jest kwadratem liczby ',i)
#         break
#     elif i+1==n:
#         print('podana liczba nie jest kwadratem innej liczby naturalnej')
        
#zad8
# n = int(input('Podaj liczbe: '))
# silnia = 1
# for i in range(1,n+1):
#     silnia *=i 
# print('silnia tej liczby wynosi: ', silnia)

#zad9
n = int(input('podaj liczbe: '))
m = int(input('podaj do ktorej potegi: '))
wynik = 1
for i in range(m):
    wynik*=n
print(wynik)