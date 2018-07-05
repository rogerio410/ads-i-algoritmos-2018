def main():
    
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    while numero_2 != 0:
        auxiliar = numero_2
        numero_2 = numero_1 % numero_2
        numero_1 = auxiliar
    print(numero_1)


if __name__ == '__main__':
    main()
