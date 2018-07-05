def main():

	numero_1 = int(input())
	numero_2 = int(input())

	result = mdc(numero_1, numero_2)

	print("MDC = %d " % result)


def mdc(dividendo, divisor):
	while divisor != 0:
		c = divisor
		divisor = dividendo % divisor
		dividendo = c
	return dividendo


if __name__ == '__main__':
	main()