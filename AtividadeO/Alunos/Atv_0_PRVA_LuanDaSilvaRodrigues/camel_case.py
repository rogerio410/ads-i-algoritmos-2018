def main():
	sentença = input()
	split_frase(sentença)
	
def split_frase(frase):
	qnt_palavra = 1
	for i in range(len(frase)):
		if eh_maiuscula(frase[i]):
			qnt_palavra += 1
	print(qnt_palavra)


def eh_maiuscula(letra):
	if ord(letra) >= 65 and ord(letra) <= 90:
		return True
	return False


if __name__ == '__main__':
	main()