def main():
    nb = input('Número em binário: ')
    aux = 1
    nd = 0
    for n in range(len(nb)-1, -1, -1):
        if nb[n] == '0':
            pass
        else:
            nd += int(nb[n]) * aux
        aux += aux
    print('Número em decimal:', nd)


if __name__ == '__main__':
    main()