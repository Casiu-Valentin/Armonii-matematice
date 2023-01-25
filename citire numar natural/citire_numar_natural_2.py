# Realizat de /Produced by Casiu George Valentin
"""
Se citeşte n, număr natural/It reads n, natural number
"""

def citire():# citire numar natural
	while True:
		try:
			n=int(input("Introduceti un numar natural:"))
			if n>=0:
				return n
			else:
				print("Numerele naturale sunt pozitive")
		except ValueError:
			print("Mai incearca")

print(citire())
