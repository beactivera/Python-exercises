# LICZBY PSEUDOLOSOWE
from random import randint

#zad1
# l = []
# for i in range(10):
#     l += [randint(20,100)]
# print(l)
# lmin = min(l)
# lmax = max(l)
# print('min = ', lmin, 'max = ', lmax)

#zad2
# l = []
# for i in range(10):
#     l += [randint(-5,5)]
# print(l)
# suma = 0
# for x in range(len(l)):
#     suma += l[x]
# print('suma tych elementow wynosi: ', suma)

#zad3
n = randint(1,1000)
print(n)
x = int(input('Podaj wylosowane liczbe: '))
ilosc = 1
while x != n:
    if x < n:
        print('wylosowane liczba jest wieksza od podanej')
        ilosc += 1
        x = int(input('Podaj wylosowane liczbe: '))
    elif x > n:
        print('wylosowana liczba jest mniejsza od podanej')
        ilosc+=1
        x = int(input('Podaj wylosowane liczbe: '))

print('Brawo, udalo Ci sie znalezc liczbe za ', ilosc, ' razem')
