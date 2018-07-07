def main():
    primeiro_numero = int(input('Digite o primeiro numero: '))
    segundo_numero = int(input('Digite o segundo numero: '))

    if primeiro_numero > segundo_numero:
        maior = primeiro_numero
        menor = segundo_numero
    else:
        maior = segundo_numero
        menor = primeiro_numero

    verificador = menor

    while menor % verificador + maior % verificador != 0:
        verificador -= 1

    print(verificador)


if __name__ == '__main__':
    main()
