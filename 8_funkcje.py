#zad1
def f(x):
    if x>=-1:
        x=x**2+6*x-2
        return x
    else:
        x=(5*x-3)/(x**2-1)
        return x


a=int(input('Podaj liczbe: '))
b=a+3
c=-1*a
wynik = f(a)-3*f(b)+f(c)
print(wynik)