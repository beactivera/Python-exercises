#LISTY
import copy

#zad1
l = [3,'alfa', 2.71, 'kot']
# print(l[-1])
# dla indexu < 0 , liczy elementy od tylu
# dla indexu > 0 i indexu > len(lista) program wyrzuci blad
# l[0] = 4
# l[len(l)-1] = 'pies'
# print(l)

l2=l # to nie jest kopie tylko odnosnik-reference do starej listy
l2[2]=3
print(l)
print(l2)

# l3=list(l)
l3=copy.copy(l)
l3[1]='beta'
print(l)
print(l3)
