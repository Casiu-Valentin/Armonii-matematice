# Realizat de /Produced by Casiu George Valentin
"""
Citeste un numar natural de la tastatura si afiseaza daca este prim/ Read a natural number from the keyboard and displays if it is prime
"""

import math

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def prim(a):# verifica daca un numar este prim /check if a number is prime
    if a==0 or a==1:
        ras=False
    elif a==2:
        ras=True
    else:
        ras=True
        if a%2==0: #eliminam numerele pare pentru a putea sa punem pasul 2 la for /we remove the even numbers to be able to put step 2 at for
            ras=False
        else:
            for i in range(3,round(math.sqrt(a))+1,2):
                if a%i==0:
                    ras=False
                    break
    return ras


a=citire() #programul principal/the main program
if prim(a):
    print('Numarul este prim /The number is prime')
else:
    print('Numarul nu este prim /The number is not prime')
