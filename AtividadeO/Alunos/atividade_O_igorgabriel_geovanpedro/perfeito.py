def main():
    N = int(input())
    soma = 0
    for i in range(1, N):
        if N % i == 0:
            soma += i
        else:
            pass

    if soma == N:
        print('Perfeito!')
    else:
        print('Não é perfeito!')


if __name__ == '__main__':
    main()
