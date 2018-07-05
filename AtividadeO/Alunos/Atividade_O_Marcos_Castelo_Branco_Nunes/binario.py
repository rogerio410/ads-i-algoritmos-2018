def main():
    binary = input("Digite o valor binario: ")
    decimal = 0
    for i in range(len(binary)-1,-1,-1):
        if binary[(len(binary)-1)-i] == "1":
            decimal += 2 ** i

    print(decimal)


if __name__ == "__main__":
    main()
