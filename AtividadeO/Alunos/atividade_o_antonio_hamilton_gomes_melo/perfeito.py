def main():
    # entradas
    N = int(input())
    soma = 0
    # processamento
    for i in range(1, N):
        if N % i == 0:
            soma += i
    # saidas
    if soma == N:
        print('Perfeito')
    else:
        print('Nao Perfeito')


if __name__ == '__main__':
    main()