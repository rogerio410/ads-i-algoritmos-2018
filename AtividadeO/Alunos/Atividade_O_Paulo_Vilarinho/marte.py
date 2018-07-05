def main():
    #entrada
    mensagens = input("digite a mensagem da nave espacial. ")
    #processamento
    erros = count_erros(mensagens)
    #saida
    print(erros)

def count_erros(mensagem):
    erros = 0
    aux = 1
    for i in range(len(mensagem)):
        if aux == 1 :
            if mensagem[i] != "S" :
                erros += 1
        elif aux == 2 :
            if mensagem[i] != "O" :
                erros += 1
        elif aux == 3 :
            if mensagem[i] != "S" :
                erros += 1
        if aux == 3:
            aux = 1
        else :
            aux += 1

    return erros

if __name__ == '__main__':
    main()
