# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
1+2+3+..+10=55
1+2+3+..+100=5050
1+2+3+..+1000=500500
1+2+3+..+10000=50005000
1+2+3+..+100000=5000050000
1+2+3+..+1000000=500000500000
1+2+3+..+10000000=50000005000000
1+2+3+..+100000000=5000000050000000
1+2+3+..+1000000000=500000000500000000
1+2+3+..+10000000000=50000000005000000000
............................."""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def tipareste(a): # tipareste 1+2+3+..+100.... unde a reprezinta numarul de 0-uri /print 1+2+3+..+100.... where a reprezents the number of 0s
    t = a * (a + 1) // 2
    print("1+2+3+..+" + str(a) + "=" + str(t))

n = citire() #programul principal /the main program
for i in range(1, n + 1):
    tipareste(10 ** i)
