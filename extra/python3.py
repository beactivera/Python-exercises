#zad3 
tab = [[0 for col in range(10)] for row in range(10)]
for i in range(1,11,1):
    for y in range(1,11,1):
        tab[i-1][y-1] = "*"
    print(tab[i-1])
