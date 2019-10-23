import re

for _ in range(int(input())):
	N=input()				#[-+]
	print(bool(re.match(r"^[-|+]?\d*\.\d+$", N)))
						#ya sea - + o digit(os/o) seguidos por un . despues los decimales $ indica que deben ser hasta el final por eso si encuentra un caracter peta