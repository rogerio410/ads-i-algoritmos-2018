def main():
    limite_maior = int(input('Maior: '))
    limite_menor = int(input('Menor: '))

    #for i in range(limite_maior - 1, limite_menor, -1):
    for i in range(limite_menor + 1, limite_maior):
        numero_atual = i
        if primo(numero_atual):
            print(numero_atual)


def primo(numero):
    #for n in range(numero - 1, 1, -1):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True

if __name__ == '__main__':
    main()