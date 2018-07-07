def main():
    # entradas
    dividendo = int(input())
    divisor = int(input())
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