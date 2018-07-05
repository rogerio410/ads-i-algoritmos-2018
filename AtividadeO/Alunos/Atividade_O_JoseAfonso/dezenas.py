def main():
    #entrada
    numero = int(input('Digite um número: '))

    #processamento
    milhares = numero // 1000
    centenas = numero % 1000
    centenas_corretas = centenas // 100
    dezenas = centenas % 100
    dezenas_corretas = dezenas // 10
    unidade = dezenas % 10

    parte1 = milhares * 10
    parte2 = centenas_corretas
    resultado1 = parte1 + parte2
    print('Dezena 1 = {}'.format(resultado1))

    parte3 = dezenas_corretas * 10
    parte4 = unidade
    resultado2 = parte3 + parte4
    print('Dezena 2 = {}'.format(resultado2))

    soma_dezenas = resultado1 + resultado2

    #saída
    print('A raiz do número {} equivale a {}'.format(numero, soma_dezenas))

if __name__ == '__main__':
    main()