def main():
	imprimir_milhares()


def imprimir_milhares():
	for dezena in range(1000, 9999):
		raiz = dezena ** (1/2)
		primeira_dezena = dezena // 100
		segunda_dezena = dezena % 100

		if raiz == (primeira_dezena + segunda_dezena):
			print(dezena)


if __name__ == '__main__':
	main()