def main():
    # entrada
    numero_um = int(input())
    numero_dois = int(input())

    # Processamento
    resultado = calc_mdc(numero_um, numero_dois)

    # Saida
    print(resultado)


def calc_mdc(numero_um, numero_dois):
    minimo = 1

    if numero_um > numero_dois:
        verificador = numero_um - 1
    else:
        verificador = numero_dois - 1

    while verificador >= minimo:
        if numero_um % verificador == 0 and numero_dois % verificador == 0:
            return verificador
        verificador -= 1


if __name__ == '__main__':
    main()
