def main():

	mensagem = input()
	letras_alteradas = 0
	for i in mensagem:
		if i != 'S' and i != 'O':
			letras_alteradas = letras_alteradas + 1

	print('Quantidade de letras alteradas:', letras_alteradas)

if __name__ == '__main__':
	main()