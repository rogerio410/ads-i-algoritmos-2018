def main():
    # entrada
    n = int(input("Digite um numero N: "))

    # processamento
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i

    # saida
    if soma == n:
        print(n, "é perfeito")
    else:
        print(n, "não é perfeito")


if __name__ == "__main__":
    main()
