def main():
    num_bin = input('nimero binario: ')
    tam = len(num_bin)
    valor = 0
    for i in range(tam):
        if num_bin[i] == '1':
            valor += 2**(tam-i-1)
#            print(i, valor)
    print(valor)


if __name__ == '__main__':
    main()

