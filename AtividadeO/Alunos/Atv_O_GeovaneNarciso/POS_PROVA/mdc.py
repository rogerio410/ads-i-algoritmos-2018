def main():
    # entrada
    num_1 = int(input())
    num_2 = int(input())

    # processamento
    while num_2 != 0:
        aux = num_2
        num_2 = num_1 % num_2
        num_1 = aux

    # saida
    print("MDC:", num_1)


if __name__ == '__main__':
    main()
