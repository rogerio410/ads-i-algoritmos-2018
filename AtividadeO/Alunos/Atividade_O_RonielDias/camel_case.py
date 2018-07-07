def main():
	# entrada
	frase = input()
	
	# processamento
	quantPalavras = split_frase(frase)

	# saída
	print(quantPalavras)

# recebe frase como parâmetro e retorna a quantidade de palavras que a frase compõe
def split_frase(frase):

	quantPalavras = 0
	for i in range(len(frase)):
		aux = frase[i] # recebe uma letra de frase para para ser passado como argumento para a função eh_maiuscula()
		flag = eh_maiuscula(aux)

		if(flag == 1):
			quantPalavras = quantPalavras + 1

	return quantPalavras

# recebe uma letra e retorna valor 1 se for letra maiúscula ou 0 caso não seja
def eh_maiuscula(letra):
	flag = -1
	# utiliza a tabela ascii para verificar se a letra é maiúscula
	if(ord(letra) >= 65) and (ord(letra) <=90):
		flag = 1
	else:
		flag = 0

	return flag

if __name__ == '__main__':
	main()

