# LICZBY PSEUDOLOSOWE
from random import randint
l = []
for i in range(10):
    l += [randint(20,100)]
print(l)
lmin = min(l)
lmax = max(l)
print('min = ', lmin, 'max = ', lmax)
