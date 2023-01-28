# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
15873*1*7=111111
15873*2*7=222222
15873*3*7=333333
15873*4*7=444444
15873*5*7=555555
15873*6*7=666666
15873*7*7=777777
15873*8*7=888888
15873*9*7=999999
................"""

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

a=citire() #Programul principal /The main program
for i in range(1,a):
    print("15873*"+str(i)+"*7="+str(15873*i*7))
