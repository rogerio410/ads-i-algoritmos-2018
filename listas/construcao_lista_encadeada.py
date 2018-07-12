def main():

    n = int(input('Qtd de Sublista? '))

    vetor = [None] * n

    for i in range(n):
        entrada = input('Digite e a lista: ')
        sublista = entrada.split()
        vetor[i] = sublista


    for i in range(len(vetor)):
        item = vetor[i]
        for j in range(len(item)):
            print(item[j])


if __name__ == '__main__':
    main()