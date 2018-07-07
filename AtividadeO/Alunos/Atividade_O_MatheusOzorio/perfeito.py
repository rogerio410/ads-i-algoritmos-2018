def main():
    #entrada
    N = int(input("Digite um número: "))
    contador = 0

    for i in range (1, N):
        if N % i == 0:
            contador += i

    if contador == N:
        print("O número é perfeito")


if __name__ == '__main__':
    main()