def main():
    # entrada
    num1 = int(input("Digite um numero inteiro : "))
    num2 = int(input("Digite outro numero inteiro: "))

    # processamento com saida
    mdc = num1
    while num1 % mdc != 0 or num2 % mdc !=0:
        mdc = mdc - 1
    print("MDC({},{}) = {}".format(num1, num2, mdc))


if __name__ == "__main__":
    main()
