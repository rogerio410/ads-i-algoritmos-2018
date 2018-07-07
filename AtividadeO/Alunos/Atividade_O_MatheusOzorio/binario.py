def main():
    #entrada
    bina = input("Digite o número em binário: ")
    decimal = 0

    for i in range (len(bina)):
        if bina[i] == '1':
            bina[i] == int(bina[i])
            decimal += bina[i]
    print(decimal)








if __name__ == '__main__':
    main()