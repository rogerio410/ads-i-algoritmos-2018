def main():
	n = int(input())

	somador = 0
	for i in range(1,n):
		if n % i == 0:
			somador += i

	if somador == n :
		print(n,'é perfeito.')
	else:
		print(n,'não é perfeito.')


if __name__ == '__main__':
	main()