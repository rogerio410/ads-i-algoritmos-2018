def main():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    if num1 > num2:
        i = num2
    else:
        i = num1
    while i > 0:
        if num1 % i == 0 and num2 % i == 0:
            print("MDC de %d e %d é: %d" % (num1, num2, i))
            break
        i -= 1

if __name__ == '__main__':
    main()
