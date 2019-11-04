import math

liczba = int(input("podaj liczbe: "))
while math.sqrt(liczba) * math.sqrt(liczba)==liczba:
    print('Jest to kwadrat liczby naturalnej')
    break