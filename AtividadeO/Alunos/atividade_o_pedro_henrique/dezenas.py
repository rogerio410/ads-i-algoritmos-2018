def main():
    # Processamento
    for numero in range(1000, 10000):
        parte_um = ''
        parte_dois = ''
        cont = 0
        numero_aux = str(numero)

        for digito in numero_aux:
            if cont <= 1:
                parte_um += digito
            else:
                parte_dois += digito

            cont += 1

        parte_um = int(parte_um)
        parte_dois = int(parte_dois)

        soma = parte_um + parte_dois
        if soma_eh_igual_a_raiz(numero, soma):
            print(numero)


def soma_eh_igual_a_raiz(digito, soma):
    numero = soma * soma
    return numero == digito


if __name__ == '__main__':
    main()
