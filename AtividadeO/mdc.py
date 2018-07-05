def main():
    maior = int(input('Valor maior: '))
    menor = int(input('Valor menor: '))

    mdc = menor
    resto = maior % menor

    while resto != 0:
        maior = menor
        menor = resto
        resto = maior % menor
        mdc = menor

    print("O MDC eh: ", mdc)


if __name__ == '__main__':
    main()