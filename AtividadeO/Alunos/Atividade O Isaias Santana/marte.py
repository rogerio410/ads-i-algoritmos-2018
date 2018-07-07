def main():
    mensagem = input()
    cont = 0
    if mensagem.count("S") > 1:
        cont += 2
    if mensagem.count("O") > 1:
        cont += 1
    print(cont)


if __name__ == '__main__':
    main()