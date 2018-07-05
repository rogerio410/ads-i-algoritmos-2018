def main():
    numero = input()

    bin = binario(numero)

    print("Numero decimal = %d" % bin)

def binario(num):
    num_decimal = 0

    num = num[::-1]

    for i in range(len(num)):
        if num[i] == "i":
            num_decimal += 2**1

    return num_decimal

if __name__ == '__main__':
    main()