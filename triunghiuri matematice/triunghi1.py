# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
1
232
34543
.............
890123454321098
90123456765432109
0123456789876543210
.....................
56789012345678987654321098765
6789012345678901098765432109876
.................................
"""

def succesor(k):
    if k==9:
        return 0
    else:
        return k+1
def predecesor(k):
    if k==0:
        return 9
    else:
        return k-1

def citire(text):# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input(text)
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

#Programul principal/The main program
n=citire("Introduceti numarul de linii/Enter number of rows:")
x=0
for i in range(1,n+1):
    x=succesor(x)
    linie=""
    t=x
    for j in range(1,i+1):
        linie+=str(t)
        t=succesor(t)
    t=predecesor(predecesor(t))
    for j in range(1,i):
        linie+=str(t)
        t=predecesor(t)
    print(linie)