def czy_pierwsza(n): 

    for x in range(2, n//2):
        if n % x == 0:
            return False

    return True

def stworz_liste(a, b=10):

    lista_pierwszych = []

    while len(lista_pierwszych) != b:

        if czy_pierwsza(a):
            lista_pierwszych.append(a)

        a += 1

    return lista_pierwszych