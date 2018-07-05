def main():
    # entrada
    s = input('Digite a mensagem:')

    # contador
    letras_alteradas = 0

    # processamento
    for i in range(0, len(s), +3):
        if s[i] != 'S':
            letras_alteradas += 1
        if s[i + 1] != 'O':
            letras_alteradas += 1
        if s[i + 2] != 'S':
            letras_alteradas += 1

    # saida
    print(letras_alteradas)


if __name__ == '__main__':
    main()