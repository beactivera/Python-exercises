#zad3 
# tab = [[0 for col in range(10)] for row in range(10)]
# for i in range(1,11,1):
#     for y in range(1,11,1):
#         tab[i-1][y-1] = "*"
#     print(tab[i-1])

#zad4
# tab = [[0 for col in range(10)] for row in range(10)]
# for i in range(1,11,1):
#     for y in range(1,11,1):
#         tab[0][y-1] = "*"
#         tab[i-1][0] = '*'
#         tab[9][y-1] = '*'
#         tab[i-1][9] = '*'
#     print(tab[i-1])

#zad5
tab = [[0 for col in range(10)] for row in range(10)]
for i in range(1,11,1):
    for y in range(1,11,1):
        if i == y:
            tab[i-1][y-1] = "*"
        else:
            tab[i-1][y-1] = ' '
    print(tab[i-1])