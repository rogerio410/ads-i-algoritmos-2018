def main():
    for numero in range(1000,10000):
        numero = str(numero)
        primeira_dezena = numero[0:2]
        segunda_dezena = numero[2:]
        primeira_dezena = int(primeira_dezena)
        segunda_dezena = int(segunda_dezena)
        numero = int(numero)
        raiz_de_numero = numero ** (1/2)
        soma = primeira_dezena + segunda_dezena
        if raiz_de_numero == soma:
            print(numero)

if __name__=='__main__':
    main()