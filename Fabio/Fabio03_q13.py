def main():

    n = int(input())
    maior = int(input())

    for i in range(n-1):
        numero = int(input())
        if numero > maior:
            maior = numero

    print(maior)


if __name__ == '__main__':
    main()