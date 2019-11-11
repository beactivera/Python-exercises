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
l = []
for i in range(10):
    l += [randint(-5,5)]
print(l)
suma = 0
for x in range(len(l)):
    suma += l[x]
print('suma tych elementow wynosi: ', suma)
