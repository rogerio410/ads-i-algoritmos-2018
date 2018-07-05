def main():
	a,b = map(int, input().split())

	a, b = maior(a,b)

	subtraçao = a - b
	
	while  subtraçao > 0 :
		a = b
		b = subtraçao
		subtraçao = a - b

	print(a)	
	

def maior(a,b):
	if a > b:
		maior = a
		menor = b
	else:
		maior = b
		menor = a
	return maior, menor


if __name__ == '__main__':
	main()