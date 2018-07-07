def main():
    for n in range(1000, 9999):
        d1 = n // 100
        d2 = n % 100
        soma = d1 + d2
        for i in range(n):
            if i * i == n:
                raiz = i
                if soma == raiz:
                    print(n)


if __name__ == '__main__':
    main()