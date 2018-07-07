def main():
	mensagem = input()
	contador = 0

	qnt = len(mensagem) // 3 #qnt de loops

	for i in range(qnt):
		palavra_quebrada = mensagem[:3]  # SLICE NAO PERMITIDO
		
		if verificar_letra_diferente(palavra_quebrada):
			contador += 1

		mensagem = mensagem[3:]  # SLICE NAO PERMITIDO
	
	print(contador)


def verificar_letra_diferente(palavra): #Recebe palavra só com 3 letras
	for i in range(3):
		if palavra[i] != 'S' and palavra[i] != 'O':
			return True
	return False


if __name__ == '__main__':
	main()