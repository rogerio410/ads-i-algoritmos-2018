def main():
    def converter(numero):
        decimal = 0
        numero = str(numero)
        numero = numero[::-1]  # dont use it
        tamanho = len(numero)
        for i in range(tamanho):
            if numero[i] == '1':
                decimal = decimal+2**i
        return decimal

    n = int(input())
    b = converter(n)
    print(b)


if __name__ == '__main__':
    main()
