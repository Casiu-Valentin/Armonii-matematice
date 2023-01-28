# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
1*9+2=11
21*9+33=222
321*9+444=3333
4321*9+5555=44444
54321*9+66666=555555
654321*9+777777=6666666
............................."""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def nr1(a): # formeaza primul numar din expresie /form the first number in the expression
    b=0
    for i in range(a):
        b += (i+1) * 10 ** i
    return b

def nr2(a): # formeaza al doilea numar din expresie /forms the second number in the expression
    b=0
    for i in range(a):
        b+=(a+1)*10**i
    return b


n= citire() #programul principal /the main program
for a in range(1,n):
    print(str(nr1(a))+"*9+"+str(nr2(a))+"="+str(nr1(a)*9+nr2(a)))
