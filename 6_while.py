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
# liczba = random.randint(13,100)
# print(liczba)
# x = int(input('Jaka liczbe wylosowal program? '))
# # print(x)
# proba = 1
# while x!=liczba:
#     x = int(input('Jaka liczbe wylosowal program? '))
#     proba +=1
#     if x == 'q':
#         print("liczba szukana to: ", liczba, "wykonales ", proba, " prob")
# print('Brawo! Odgadles liczbe po ', proba, ' probach')

#zad9
# dobrze=0
# while dobrze<3:
#     a=random.randint(100,1000)
#     b=random.randint(100,1000)
#     dodawanie = a,b
#     print(dodawanie)
#     wynik = int(input('Podaj wynik dodawania tych liczb: '))
#     if wynik !=a+b:
#         dobrze = 0
#     else:
#         dobrze+=1
# print('Gratulacje! dobry wynik trzy razy pod rzad!')

#zad10
# D={}
# produkt=input('Podaj nazwe produktu: ')
# while produkt != "quit":
#     if produkt in D.keys():
#         cena=input('Produkt juz istnieje, podaj jego cene: ')
#         D2={produkt:cena}
#         # print(D2)
#         D.update(D2)
#     else:
#         cena = input('Podaj cene produktu: ')
#         D[produkt]=cena
#     produkt=input('Podaj nazwe produktu: ')
# print('Oto nasz spis: ', D)

#zad11
# lista=['O','R']
# sloneczka=100
# while sloneczka>0 and sloneczka!=2*100:
#     liczba =random.choice(lista)
#     print(liczba)
#     x=input("Orzel czy reszka? (O/R): ")
#     if x == liczba:
#         sloneczka+=9
#         print(sloneczka)
#     else:
#         sloneczka-=10
#         print(sloneczka)
# if sloneczka == 200:
#     print('Uzyskales 200 sloneczek!')
# elif sloneczka == 0 or sloneczka<0:
#     print('Nie stać Cię na kolejną runde!')

#zad12
# a=1
# b=1
# c=1
# while 0<a<=b<=c<=100:
#     n=int(input('Podaj ile chcesz wyswietlic trojek pitagorejskich: '))
#     licznik = 0
#     for k in range(1,100):
#         for m in range(1,100):
#             if licznik <n:
#                 if k>m and (k+m)%2!=0:
#                     a=k**2-m**2
#                     b=2*k*m
#                     c=k**2+m**2
#                     if a>b:# if a>b and a<b
#                         print('(',b,',',a,',',c,')')
#                     else:
#                         print('(',a,',',b,',',c,')')
#                     licznik+=1
#             else:
#                 break

# print('koniec')

# n=int(input('Podaj liczbe: '))
# x=0
# b=0
# while(x!=n):
#     for a in range(1,b):
#         c=(a*a+b*b)**0.5
#         if c%1==0:
#             print(a,b,int(c))
#             x+=1
#             if x==10:
#                 break
#     b+=1
    

n=int(input("Podaj liczbe naturalna: "))
while n != 0:
    for a in range(1,101):
        for b in range(a,101):
            for c in range(b,101):
                if math.pow(a,2) + math.pow(b,2) == math.pow(c,2) and n!=0:
                    print(a,b,c)
                    n = n - 1
                elif a==b==c==100:
                    n==0
                elif n==0:
                    break
