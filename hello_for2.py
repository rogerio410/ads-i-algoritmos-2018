def main():
    # python3 hello_for.py < nomes.txt
    while True:
        try:
            nome = input()
            tamanho = len(nome)

            for indice in range(tamanho - 1, -1, -1):
                letra = nome[indice]
                print(indice, letra)

            print('Nome:', nome)
        except:
            break

if __name__ == '__main__':
    main()