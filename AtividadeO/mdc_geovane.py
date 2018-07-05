def main():
    maior = int(input('Valor maior: '))
    menor = int(input('Valor menor: '))

    while menor != 0:
        aux = menor
        menor = maior % menor
        maior = aux

    print("O MDC eh: ", maior)


if __name__ == '__main__':
    main()