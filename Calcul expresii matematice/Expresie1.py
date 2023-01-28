# Realizat de /Produced by Casiu George Valentin
"""
Se citeşte n, număr natural. Să se evalueze expresia de mai jos/ It reads n, natural number. Evaluate the expresion below:
E=E1+E2+.....+En
unde/where Ei=1/1+1/1*2+1/1*2*3+......+1/1*2*...*i
"""

def citire(text):# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input(text)
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)


n=citire("Introduceti un numar natural/Enter a natural number:")#Programul principal/The main program
p=1
s=0
for i in range(1,n+1):
    p*=i
    pn=1/p
    s+=pn
print("E=", s)
