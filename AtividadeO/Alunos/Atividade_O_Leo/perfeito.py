def main():
	
	Numero = int(input())

	Perfeito = eh_perfeito(Numero)

	print("O Numero eh", Perfeito)

def eh_perfeito(num):
    soma = 0
    for i in range(1, num):
    	if num % i == 0:
    	    soma += i

    if num == soma:
    		return "Perfeito"
    else:
    	return "Não perfeito"


if __name__ == '__main__':
	main()