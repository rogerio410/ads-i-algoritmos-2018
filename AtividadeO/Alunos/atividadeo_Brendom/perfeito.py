def main():
    soma = 0
    divisores = ""
    soma_divisores = ""

    # entrada
    n = int(input())

    # trabalho
    for i in range(1, n):
        if n % i == 0:
            soma += i
            divisores += str(i) + " + "
        if i > n:
            break
    for j in range(len(divisores) - 3):
        letras_divisores = divisores[j]
        soma_divisores += letras_divisores
    # saidas
    if soma == n:
        # print(n,"é perfeito, pois",soma_divisores,"=",n )
        print("é perfeito")
    else:
        print("não é perfeito")


if __name__ == '__main__':
    main()
