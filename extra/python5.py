#LISTY
import copy

#zad1
# l = [3,'alfa', 2.71, 'kot']
# # print(l[-1])
# # dla indexu < 0 , liczy elementy od tylu
# # dla indexu > 0 i indexu > len(lista) program wyrzuci blad
# # l[0] = 4
# # l[len(l)-1] = 'pies'
# # print(l)

# l2=l # to nie jest kopie tylko odnosnik-reference do starej listy
# l2[2]=3
# print(l)
# print(l2)

# # l3=list(l)
# l3=copy.copy(l)
# l3[1]='beta'
# print(l)
# print(l3)

# zad2
# l = []
# # for i in range(10):
# #     l = l + [i**2]
# # print(l)
# for i in range(10):
#     if i%2 == 0:
#         l = l + [-(i**2)]
#     else:
#         l = l + [i**2]
# print(l)

# zad3
# n = int(input('Podaj ilosc liczb do wypisania: '))
# l = []

# for i in range(n):
#     m = int(input('Podaj liczbe: '))
#     l += [m]
# print(l)
# lmin = min(l)
# lmax = max(l)
# print('min = ', lmin, 'max = ', lmax)

#zad5
l = []
for i in range(100, 151):
    l += [i]
print(l)

for x in range(9):
    del l[(4*x)]
print(l)

