def main():
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    while True:
        aux = n2
        n2 = n1 % n2
        n1 = aux
        if n2 == 0:
            break

    print('MDC:', aux)
if __name__ == '__main__':
    main()