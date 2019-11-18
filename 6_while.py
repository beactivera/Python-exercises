import math
import random

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
# n=1000
# while (1/n)<0.0043212:
#     # print(n)
#     n-=1
# print("najmniejsza liczba naturalna to: ",n+1)

#zad4
# n=1
# suma=0
# while suma<11:
#     suma+=1/n
#     n+=1
# print(n)

#zad5
# l=['a']
# znak = input("podaj znaki: ")
# # print(znak)
# while znak != 'stop':
#     l.append(znak)
#     znak = input("podaj kolejny znak: ")
# print(l)

#zad6
# a = int(input('Podaj pierwsza liczbe: '))
# b = int(input('Podaj druga liczbe: '))
# while b!=0:
#     r=a%b
#     a=b
#     b=r
# print("NWD tych liczb: " a)

#zad7
# a = input('Podaj pierwszy wyraz: ')
# b = input('Podaj drugi wyraz: ')
# lancuch = ''
# while len(a) != len(b):
#     print(lancuch) 
# for i in range(len(a)):
#     lancuch = lancuch + a[i] + b[i]
# print(lancuch)        

#zad8
liczba = random.randint(13,100)
print(liczba)
x = int(input('Jaka liczbe wylosowal program? '))
# print(x)
proba = 1
while x!=liczba:
    x = int(input('Jaka liczbe wylosowal program? '))
    proba +=1
    if x == 'q':
        print("liczba szukana to: ", liczba, "wykonales ", proba, " prob")
print('Brawo! Odgadles liczbe po ', proba, ' probach')
