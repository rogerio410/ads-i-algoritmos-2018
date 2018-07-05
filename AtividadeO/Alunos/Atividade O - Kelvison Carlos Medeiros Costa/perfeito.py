def main():
    # entrada
    N = int(input())
    multiplos = 0

    # processamento
    for i in range(1, N):
        if N % i == 0:
            multiplos += i
    # saida
    if multiplos == N:
        print('N é perfeito')
    else:
        print('N não é perfeito')

if __name__ == '__main__':
    main()