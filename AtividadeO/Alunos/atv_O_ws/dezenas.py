def main():
    # Entrada
    milhar = input('Digite um número de 4 digitos: ')

    # Processamento
    dezena1 = int(milhar[0] + milhar[1])
    dezena2 = int(milhar[2] + milhar[3])
    raiz = int(milhar)**(1/2)

    # Saida
    if dezena1 + dezena2 == raiz:
        print('A soma de {} com {} é IGUAL a raiz de {} que é {}.'.format(dezena1, dezena2, milhar, raiz))
    else:
        print('A soma de {} com {} é DIFERENTE a raiz de {} que é {}.'.format(dezena1, dezena2, milhar, raiz))


if __name__ == '__main__':
    main()
