def main():
    # entradas
    num1, num2 = int(input('Número 1:')), int(input('Número 2:'))

    # processamento
    while True:
        aux = num2
        num2 = num1 % num2
        num1 = aux
        if num2 == 0:
            break

    # saida
    print(aux)


if __name__ == '__main__':
    main()
