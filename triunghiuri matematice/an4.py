# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
9³=729
99³=970299
999³=997002999
9999³=999700029999
99999³=999970000299999
999999³=999997000002999999
9999999³=999999700000029999999
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

a = int(input("Introduceti numarul de linii care le doriti afisate:"))  #programul principal /the main program
for i in range(1, a + 1):
    t = nr(i)
    print(str(t)+"³="+str(t ** 3))