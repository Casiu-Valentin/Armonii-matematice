# Realizat de /Produced by Casiu George Valentin
"""
Se citeşte n, număr natural/It reads n, natural number
"""

def citire():# citire numar natural/ Natural number reading
	while True:
		try:
			n=int(input("Introduceti un numar natural/Enter a natural number:"))
			if n>=0:
				return n
			else:
				print("Numerele naturale sunt pozitive/Natural number a positive")
		except ValueError:
			print("Mai incearca/Try again")

print(citire())
