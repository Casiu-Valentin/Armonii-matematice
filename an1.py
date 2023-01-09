"""
Afiseaza: /Display:
1^2=1
11^2=121
101^2=10201
1001^2=1002001
10001^2=100020001
100001^2=10000200001
1000001^2=1000002000001
............................."""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def nr(a): #formeaza numerele care trebuie ridicate la patrat conform schitei de inceput / form the number that must be squred according to the initial sketch
    if a==1:
        b=1
    else:
        b = 1 + 10 ** (a - 1)
    return b

a=citire() #programul principal /the main program
for i in range(1, a + 1):
    t = nr(i)
    print(str(t)+"^2="+str(t ** 2))