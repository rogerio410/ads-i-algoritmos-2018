def main():
	binario = input()

	natural = 0
	expoente = len(binario) - 1
	for i in range(len(binario)):
		natural += int(binario[i]) * 2 ** expoente
		expoente -= 1
	print(natural)


if __name__ == '__main__':
	main()