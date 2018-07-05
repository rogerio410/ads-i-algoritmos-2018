def main():
    S = input("Digite a mensagem: ")
    n_interferencias = 0
    for i in range(0, len(S), 3):
        if S[i] != "S":
            n_interferencias += 1
        if S[i+1] != "O":
            n_interferencias += 1
        if S[i+2] != "S":
            n_interferencias += 1

    print(n_interferencias)


if __name__ == '__main__':
    main()
