# Realizat de /Produced by Casiu George Valentin
"""
Toate numerele care se pot descompune in suma a trei patrate/All the numbers that can be descomposed into the sum of three squares
Afiseaza: /Display:
1. 6=1²+1²+2²
2. 9=1²+2²+2²
3. 11=1²+1²+3²
4. 12=2²+2²+2²
5. 14=1²+2²+3²
........
"""

import math

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def sd3p(n):# descompune un numar in suma a trei patrate/ descompose a number into the sum of three squares
    global z
    for i in range(1,int(math.sqrt(n))):
        for j in range(i,int(math.sqrt(n))):
            if n-i**2-j**2>0:
                t=math.sqrt(n-i**2-j**2)
            else:
                break
            if t==round(t) and i<=t and j<=t:
                print(str(z)+'. '+str(n)+"="+str(i)+"²+"+str(j)+"²+"+str(int(t))+"²")
                z+=1


a=citire()# Programul principal /The main program
z=1
for i in range(a+1):
    sd3p(i)
