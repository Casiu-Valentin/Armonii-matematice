# Realizat de /Produced by Casiu George Valentin
"""
Teorema lui Pitagora intr-un triunghi dreptunghic/Pythagoras' theorem in a right triangle:c²=a²+b²
Afiseaza: /Display:
1. 5²=3²+4²
2. 10²=6²+8²
3. 13²=5²+12²
4. 15²=9²+12²
5. 17²=8²+15²
6. 20²=12²+16²
7. 25²=7²+24²
8. 25²=15²+20²
........
"""

import math

def citire(text):# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input(text)
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def  numerepitagoreice(n):
    global z
    for i in range(1,int(n)):
        t=math.sqrt(n**2-i**2)
        if t==round(t) and i<t:
            print(str(z)+'. '+str(n)+"²="+str(i)+"²+"+str(int(t))+"²")
            z+=1


n=citire("Introduceti un numar natural/Enter natural number:")# Programul principal /The main program
z=1
for i in range(a+1):
    numerepitagoreice(i)
