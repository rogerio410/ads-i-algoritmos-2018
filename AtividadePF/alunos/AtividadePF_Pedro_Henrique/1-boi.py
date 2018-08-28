def main():
    print('===============================================')
    codigo = int(input('Digite o codigo do boi: (0 - Finaliza algoritmo): '))
    peso = float(input('Digite o peso do boi em Kg: '))

    codigo_magro = codigo
    peso_magro = peso
    codigo_gordo = codigo
    peso_gordo = peso

    peso_total = 0
    qtd_boi = 0

    while codigo != 0:
        qtd_boi += 1
        peso_total += peso

        if peso > peso_gordo:
            codigo_gordo = codigo
            peso_gordo = peso
        if peso < peso_magro:
            codigo_magro = codigo
            peso_magro = peso

        print('===============================================')
        codigo = int(input('Digite o codigo do boi: (0 - Finaliza algoritmo): '))
        peso = float(input('Digite o peso do boi em Kg: '))

    media_do_peso = peso_total / qtd_boi

    print('O boi mais magro é o boi do código %d com o peso %.2f Kg' % (codigo_magro, peso_magro))
    print('O boi mais gordo é o boi do código %d com o peso %.2f Kg' % (codigo_gordo, peso_gordo))
    print('A média do peso de todos os bois é %.2f Kg' % media_do_peso)
    print('Quantidade total de bois é igual a %d' % qtd_boi)


if __name__ == '__main__':
    main()
