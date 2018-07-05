def main():
    # entrada
    num = int(input("Digite um numero inteiro 'N': "))

    # processamento
    soma = 0
    for i in range(1, num):  #Loop de 1 até N e ira verificar se o número é divisivel por N. Ou seja: PERFEITO
        if num % i == 0:
            soma += i
    if soma == num:
        print("O número {}, é PERFEITO".format(num))
    else:
        print("O número {}, NÃO é perfeito.".format(num))


if __name__ == "__main__":
    main()
