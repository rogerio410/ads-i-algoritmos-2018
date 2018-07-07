def main():
    #entrada
    mensagem = input("Mensagem da Curiosity: ")
    contador = 0

    #processamento
    for i in range (len(mensagem)):
        if mensagem[i] != "S" and mensagem[i] != "O":
            contador +=1

    #saida
    print(contador)

if __name__ == '__main__':
    main()