def main():
    # Entrada
    mensagem = input()

    # Processamento
    letras_alteradas = 0

    for i in range(len(mensagem)):
        letra = mensagem[i]

        if letra != 'S' and letra != 'O':
            letras_alteradas += 1

    # Saída
    print(letras_alteradas)


if __name__ == "__main__":
    main()
