import math

#zad1
# liczba = int(input("podaj liczbe: "))
# while math.sqrt(liczba) * math.sqrt(liczba)==liczba:
#     print('Jest to kwadrat liczby naturalnej')
#     break

#zad2
# k=int(input("podaj liczbe naturalna: "))
# n=0
# while pow(2,n)<=k:
#     m=pow(2,n)
#     print(m)
#     n+=1

#zad3
n=1000
while (1/n)<0.0043212:
    # print(n)
    n-=1
print("najmniejsza liczba naturalna to: ",n+1)