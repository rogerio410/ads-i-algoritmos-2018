def main():
    # python3 hello_for.py < nomes.txt
    while True:
        try:
            nome = input()

            for letra in nome:
                print(letra)

            print('Nome:', nome)
        except:
            break

if __name__ == '__main__':
    main()