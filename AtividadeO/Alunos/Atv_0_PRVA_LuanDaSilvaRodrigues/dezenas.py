def main():
	for i in range(1000, 10000):
		algarismo = i

		a = algarismo // 100
		b = algarismo % 100

		raiz = algarismo ** (1/2)

		if a + b == raiz:
			print(algarismo)


if __name__ == '__main__':
	main()