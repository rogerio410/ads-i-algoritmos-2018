def main():
    #entrada
    N = int(input('Digite um número: '))
    soma = 0
    #processamento
    for i in range(1, N):
        if N % i == 0:
            soma += i
    #saida
    if N == soma:
        print('N É perfeito')
    else:
        print('N Não é perfeito')

if __name__ == '__main__':
    main()
