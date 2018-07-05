def main():
    """
        n = input()
        dezena1 = n[0] + n[1]
        dezena2 = n[2] + n[3]
        soma = int(dezena1)+int(dezena2)
    """
    for i in range(1000, 9999+1):
        i = str(i)
        d1 = i[0] + i[1]
        d2 = i[2] + i[3]
        soma = int(d1)+int(d2)
        if soma * soma == int(i):
            print(int(i), 'tem raiz exata')


if __name__ == '__main__':
    main()
