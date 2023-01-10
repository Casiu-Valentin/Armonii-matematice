# Realizat de /Produced by Casiu George Valentin
"""
Afiseaza: /Display:
1²-79*1+1601=1523   este numar prim /is prime number
2²-79*2+1601=1447   este numar prim /is prime number
3²-79*3+1601=1373   este numar prim /is prime number
4²-79*4+1601=1301   este numar prim /is prime number
5²-79*5+1601=1231   este numar prim /is prime number
6²-79*6+1601=1163   este numar prim /is prime number
7²-79*7+1601=1097   este numar prim /is prime number
8²-79*8+1601=1033   este numar prim /is prime number
9²-79*9+1601=971   este numar prim /is prime number """


for i in range(1,10): #Programul principal /The main program
    print(str(i)+"²-79*"+str(i)+"+1601="+str(i**2-79*i+1601)+"   este numar prim /is prime number")