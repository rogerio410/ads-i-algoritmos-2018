def main(): #### SAUDADES TEMPO###
    # entrada
    num = str(input("Digite um numero binario"))

    n = " "
    binario = " "
    while True:
        binario = binario + str((n % 2))
        n = n//2
        if n == 0:
            break
        binario = binario[::-1]  # NAO PERMITIDO SLICE
        binario = int(binario)

    def bin_for_dec(n):
        if n == 0:
            return ''
        else:
            return bin_for_dec(n // 2) + str(n % 2)
    print()
if __name__ == "__main__":
    main()
