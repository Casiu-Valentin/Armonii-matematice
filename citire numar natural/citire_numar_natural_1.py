def citire():# citire numar natural
    n=''
    while not(n.isdecimal()): # daca n nu e zecimal
        n = input("Introduceti un numar natural:")
        n = n.strip(' +')# elimina spatiile libere si '+' de la inceputul si sfarsitul numarului
    return int(n)

print(citire())