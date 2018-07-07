def main():
    numero_binario = input()
    cont = 0
    for i in range(1, len(numero_binario)):
        for j in numero_binario:
            cont += (2*int(j))**i

    print(cont)


if __name__ == '__main__':
    main()