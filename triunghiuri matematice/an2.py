"""
Afiseaza: /Display:
1²=1
11²=121
111²=12321
1111²=1234321
11111²=123454321
111111²=12345654321
1111111²=1234567654321
11111111²=123456787654321
111111111²=12345678987654321"""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def nr(a): #formeaza numerele care trebuie ridicate la patrat conform schitei de inceput / form the number that must be squred according to the initial sketch
    b=1
    for i in range(1,a):
        b += 10 ** i
    return b

a = 9  #programul principal /the main program
for i in range(1, a + 1):
    t = nr(i)
    print(str(t)+"²="+str(t ** 2))