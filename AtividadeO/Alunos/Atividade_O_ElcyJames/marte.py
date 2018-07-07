def main():
    s = input('Mensagem: ')
    letra = 0
    aux = 0
    for i in range(1,len(s)):
        if aux <= 3:
            if i % 2 == 0:
                if s[i] != 'S':
                    letra += 1
            else:
                if s[i] != '0':
                    letra += 1
        else:
            if i % 2 == 0:
                if s[i] != 'S':
                    letra += 1
            else:
                if s[i] != 'O':
                    letra += 1
            aux = 0
        aux += 1
    print(letra)


if __name__ == '__main__':
    main()