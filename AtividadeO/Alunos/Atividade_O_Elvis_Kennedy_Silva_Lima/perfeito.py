def main():

	N = int(input())
	soma = 0
	
	for i in range(1, N):
		if N % i == 0:
			soma = soma + i

	if soma == N:
		print('Este numero é perfeito.')
	else:
		print('Este numero não é perfeito.')

if __name__ == '__main__':
	main()