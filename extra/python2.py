#petle

n = int(input('podaj poczatkowa liczbe zakresu: '))
m = int(input('podaj koncowa liczbe zakresu: '))
#przedzial rosnacy
# for i in range(n,m+1):
#     print(i)
#przedzial malejacy
# for i in range(n, m-1, -1):
#     print(i)
#przedzial uniwersalny
if n<m:
    for i in range(n,m+1):
        print(i)
else:
    for i in range(n, m-1, -1):
         print(i)
