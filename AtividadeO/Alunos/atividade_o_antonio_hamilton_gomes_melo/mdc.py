def main():
    # entradas
    dividendo = 24
    divisor = 15
    resto = 1
    # processamento
    while resto > 0:
        resto = dividendo % divisor
        if resto > 0:
            dividendo = divisor
            divisor = resto
    # saida
    print(divisor)


if __name__ == '__main__':
    main()