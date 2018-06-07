def main():
    # python3 hello_for.py < nomes.txt
    while True:
        try:
            nome = input()
            tamanho = len(nome)
            indice = 0

            while indice < tamanho:
                print(indice, nome[indice])
                indice = indice + 1

            print('Nome:', nome)
        except:
            break

if __name__ == '__main__':
    main()