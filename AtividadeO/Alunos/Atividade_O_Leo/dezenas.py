def main():
	
	milhares()

def milhares():
	for Dezena in range(1000, 9999):
		Raiz = Dezena ** (1//2)
		Dezena1 = Dezena // 100
		Dezena2 = Dezena % 100

		if Raiz == (Dezena1 + Dezena2):
			print(Dezena)

if __name__ == '__main__':
	main()

