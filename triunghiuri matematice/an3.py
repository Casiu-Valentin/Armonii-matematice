# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
9²=81
99²=9801
999²=998001
9999²=99980001
99999²=9999800001
999999²=999998000001
9999999²=99999980000001
............................."""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def nr(a): #formeaza numerele care trebuie ridicate la patrat conform schitei de inceput / form the number that must be squred according to the initial sketch
    b=9
    for i in range(1,a):
        b += 9*10 ** i
    return b

a = int(input("Introduceti numarul de linii care le doriti afisate:")) #programul principal /the main program
for i in range(1, a + 1):
    t = nr(i)
    print(str(t)+"²="+str(t ** 2))
