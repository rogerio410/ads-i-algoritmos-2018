def main():
	
	Numero = input().split()
	Numero_1 = int(Numero[0])
	Numero_2 = int(Numero[1])

	Result = mdc(Numero_1, Numero_2)

	print(Result)

def mdc (divisor, dividendo):
	while divisor != 0:
	    c = divisor
	    divisor = dividendo % divisor
	    dividendo = c
	return dividendo

	    
if __name__ == '__main__':
	main()