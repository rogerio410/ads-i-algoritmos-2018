def main():
    def mdc(dividendo, divisor):
        while divisor != 0:
            c = divisor
            divisor = dividendo % divisor
            dividendo = c
        return dividendo

    #print(mdc(24, 15))
    print(mdc(int(input()), int(input())))


if __name__ == '__main__':
    main()
