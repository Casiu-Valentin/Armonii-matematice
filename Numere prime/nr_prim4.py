# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
Toate perechile diferite de numere prime care au si inversul prim/ All different pairs of prime number thats also  have a prime inverse
1. 13 si numarul 31 sunt prime/are prime
2. 17 si numarul 71 sunt prime/are prime
3. 37 si numarul 73 sunt prime/are prime
4. 79 si numarul 97 sunt prime/are prime
5. 107 si numarul 701 sunt prime/are prime
.............................
17. 739 si numarul 937 sunt prime/are prime
18. 769 si numarul 967 sunt prime/are prime
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
    return ras

a=citire()# Programul principal /The main program
t=1
for i in range (a): #
    if prim(i) and prim(int(str(i)[::-1])) and i<int(str(i)[::-1]): #ultima conditie este pentru a nu repeta perechile ex: 13,31 si 31,13 si pentru a fi diferite ex:101,101
        print(str(t)+'. '+str(i)+" si numarul "+ str(i)[::-1]+" sunt prime/are prime")
        t+=1