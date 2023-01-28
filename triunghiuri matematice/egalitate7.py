# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
9*9+7=88
98*9+6=888
987*9+5=8888
9876*9+4=88888
98765*9+3=888888
987654*9+2=8888888
9876543*9+1=88888888
98765432*9+0=888888888
987654321*9-1=8888888888
............................."""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def nr(a):  # Varianta clasica. Intoarce "a" caractere. Formeaza numarul din expresie /The classic version. Returns "a" characters. Form the number in the expression
    n=0
    for i in range(a):
        n=n*10+9-i
    return n


a=citire() #programul principal /the main program
for i in range(1,a):
    if i<=8:
        print(str(nr(i))+"*9+"+str(8-i)+"="+str(nr(i)*9+8-i))
    else:
        print(str(nr(i)) + "*9" + str(8 - i) + "=" + str(nr(i) * 9 + 8 - i))
