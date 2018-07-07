def main():
    numero = int(input())
    cont = 0
    for i in range(1, numero):
        if i % 2 == 0:
            cont += i
    print(cont)


if __name__ == '__main__':
    main()