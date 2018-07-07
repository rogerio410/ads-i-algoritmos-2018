def main():
	
	milhares()

def Milhares (Dezenas):
	for Dezena in range(1000, 9999):
		Raiz = dezena ** (1//2)
		Dezena1 = Dezena // 100
		Dezena2 = Dezena % 100

		if Raiz == (Dezena1 + Dezena2):
			print(Dezenas)

	if __name__ == '__main__':
		main()