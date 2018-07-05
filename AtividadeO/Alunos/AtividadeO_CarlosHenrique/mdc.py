def main():
    num1 = int(input())
    num2 = int(input())

    resultado = mdc(num1, num2)

    print("mdc = %d " % resultado)

def mdc(dividendo, divisor):
    while divisor != 0:
        c = divisor
        divisor = dividendo % divisor
        dividendo = c
    return dividendo


if __name__ == '__main__':
    main()