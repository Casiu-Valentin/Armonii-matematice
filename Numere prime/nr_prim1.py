# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
1²+1+17=19=17+2   unde/where 17, 19 si/and 17 sunt numere prime/are prime numbers
2²+2+17=23=19+4   unde/where 17, 23 si/and 19 sunt numere prime/are prime numbers
3²+3+17=29=23+6   unde/where 17, 29 si/and 23 sunt numere prime/are prime numbers
4²+4+17=37=29+8   unde/where 17, 37 si/and 29 sunt numere prime/are prime numbers
5²+5+17=47=37+10   unde/where 17, 47 si/and 37 sunt numere prime/are prime numbers
6²+6+17=59=47+12   unde/where 17, 59 si/and 47 sunt numere prime/are prime numbers
7²+7+17=73=59+14   unde/where 17, 73 si/and 59 sunt numere prime/are prime numbers
8²+8+17=89=73+16   unde/where 17, 89 si/and 73 sunt numere prime/are prime numbers
9²+9+17=107=89+18   unde/where 17, 107 si/and 89 sunt numere prime/are prime numbers
10²+10+17=127=107+20   unde/where 17, 127 si/and 107 sunt numere prime/are prime numbers
"""

for i in range(1,11): #Programul principal /The main program
    t=i**2+i+17
    n=str(t-2*i)
    print(str(i)+"²+"+str(i)+"+17="+str(t)+"="+n+"+"+str(2*i)+"   unde/where 17, "+str(t)+' si/and '+n+" sunt numere prime/are prime numbers")