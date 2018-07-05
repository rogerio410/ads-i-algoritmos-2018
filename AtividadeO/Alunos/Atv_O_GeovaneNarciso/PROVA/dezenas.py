def main():
    # entrada

    # processamento, saida
    for i in range(1000, 10000):
        milhar = str(i)
        dezena_1 = milhar[0] + milhar[1]
        dezena_2 = milhar[2] + milhar[3]
        if int(dezena_1) + int(dezena_2) == i ** 0.5:
            print(i)


if __name__ == '__main__':
    main()
