# Realizat de /Produced by Casiu George Valentin
"""
Toate numerele prime si palindrom/All prime numbers and palindroms
Afiseaza: /Display:
1. 2 este prim si palindrom /is prime and palindrome
2. 3 este prim si palindrom /is prime and palindrome
3. 5 este prim si palindrom /is prime and palindrome
4. 7 este prim si palindrom /is prime and palindrome
5. 11 este prim si palindrom /is prime and palindrome
6. 101 este prim si palindrom /is prime and palindrome
7. 131 este prim si palindrom /is prime and palindrome
8. 151 este prim si palindrom /is prime and palindrome
9. 181 este prim si palindrom /is prime and palindrome
10. 191 este prim si palindrom /is prime and palindrome
11. 313 este prim si palindrom /is prime and palindrome
12. 353 este prim si palindrom /is prime and palindrome
.............................
Observatie /Observation:
..................................................
19. 919 este prim si palindrom /is prime and palindrome
20. 929 este prim si palindrom /is prime and palindrome
21. 10301 este prim si palindrom /is prime and palindrome
22. 10501 este prim si palindrom /is prime and palindrome
....................................................
Nu o sa avem niciodata un numar prim si palindrom cu un numar par de cifre /We will never have a prime number and palindrome with an even number of digits
Si asta datorita criteriului de divizibilitate cu 11 /And this is due to the criterium of divisibility by 11: numarul /number (abcd) divide 11 daca/if (a+c)-(b+d) divide 11
La palindrom avem /At palindrome we have: numaru /number (abba) divide 11 daca/if (a+b)-(b+a) divide 11 adica daca/that is if  0 divide 11.
Deci toate numerele palindrom cu numar par de cifre sunt divizibile cu 11 deci nu pot fi si prime. / All palindrome numbers with even digits are divisible by 11 so are no prime.
Programul se poate optimiza respectand criteriile de divizibilitate. /The program can be optimized by respecting the divisibility criteria.
Numarul nu poate incepe niciodata cu 2,4,6,8 datorita criteriului de divizibilitate cu 2. /The number can never start with 2,4,6,8 due to the criterion of divisibility by 2.
Numarul nu poate incepe niciodata cu 5 datorita criteriului de divizibilitate cu 5. /The number can never start with 5 due to the criterion of divisibility by 5.
"""

import math

def citire():# citire numar natural /natural number reading
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal /if n is not decimal
        n = input("Introduceti un numar natural /Enter a natural number:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului /remove spaces and '+' from the beginning and end of number
    return int(n)

def prim(a):# verifica daca un numar este prim /check if a number is prime
    if a==0 or a==1:
        ras=False
    elif a==2:
        ras=True
    else:
        ras=True
        if a%2==0: #eliminam numerele pare pentru a putea sa punem pasul 2 la for /we remove the even numbers to be able to put step 2 at for
            ras=False
        else:
            for i in range(3,round(math.sqrt(a))+1,2):
                if a%i==0:
                    ras=False
                    break
    return ras

def inv(a):# verifica daca un sir este palindrom /check if a string is a palindrome
    return str(a)==str(a)[::-1]


a=citire()# Programul principal /The main program
t=1
for i in range (a):
    if prim(i) and inv(i):
        print(str(t)+'. '+str(i)+" este prim si palindrom /is prime and palindrome ")
        t+=1
