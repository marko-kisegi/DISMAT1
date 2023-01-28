#dislab1
import math

def kvadratna(a, b, c): # (+b +- sqrt (b^2 + 4ac)) / 2*a jer a(n+2)-l1a(n+1)-l2a(n) = 0
    a, b, c = a, b, c
    korijen = math.sqrt( math.pow(b,2) + 4 * a * c )
    nazivnik = 2 * a
    x1 = (b - korijen) / nazivnik
    x2 = (b + korijen) / nazivnik
    return x1, x2


def koef(l1, l2, a0, a1, n): # a(n+2) = l1 * an(n+1) + l2 * an 
    x1, x2 = kvadratna(1 , l1, l2)
    if(x1 == x2):
        c1 = a0
        c2 = (a1 - a0 * x1) / x2
        print(n,".ti clan niza funkcijom je", (c1*math.pow(x1,n) + (c2*math.pow(x2,n)*n)))
    else:     
        c2 = (a1 - a0 * x1) / (x2-x1)
        c1 = (a0 - c2) 
        print(n,".ti clan niza funkcijom je", (c1*math.pow(x1,n) + c2*math.pow(x2,n)))


def funkcija(l1, l2 , a0, a1, n ):
    if(n==0): return a0
    if(n==1): return a1
    koef(l1, l2, a0, a1, n)


def rekurzija(l1, l2, a0, a1, n):
    if(n==0): return a0
    if(n==1): return a1
    polje = [a0, a1]
    for i in range(2, n+1):
        polje.append(l1*polje[i-1] + l2*polje[i-2])
    print(n,".ti clan niza rekurzijom je", polje[len(polje)-1])


# l1 , l2 , a0, a1 , n
l1, l2, a0 , a1, n = 1, 1, 1, 1, 100
rekurzija(l1, l2, a0 , a1, n)
funkcija(l1, l2, a0 , a1, n)
    
