# Realizat de /Produced by Casiu George Valentin
"""
Toate numerele care se pot descompune in suma a doua patrate/ All the numbers that can be descomposed into the sum of two squares
Afiseaza: /Display:
1. 5=1²+2²
2. 10=1²+3²
3. 13=2²+3²
4. 17=1²+4²
5. 20=2²+4²
........
"""

import math

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def sd2p(n):# descompune un numar in suma a doua patrate/descompose a number into the sum of two squares
    global z
    for i in range(1,int(math.sqrt(n))):
        t=math.sqrt(n-i**2)
        if t==round(t) and i<=t:
            print(str(z)+'. '+str(n) + "=" + str(i) + "²+" + str(int(t)) + "²")
            z+=1

# Programul principal /The main program
a=citire()
z=1
for i in range(a+1):
    sd2p(i)
