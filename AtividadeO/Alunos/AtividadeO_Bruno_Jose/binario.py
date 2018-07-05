def main():
	numero = input()

	bin = binario(numero)

	print("Numero decimal = %d" % bin)


def binario(num):
	numero_decimal = 0
	
	num = num[::-1]

	for i in range(len(num)):
		if num[i] == "1":
			numero_decimal += 2**i
	
	return numero_decimal


if __name__ == '__main__':
	main()