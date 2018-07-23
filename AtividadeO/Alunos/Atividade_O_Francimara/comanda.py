def main():
    # entrada
    menu = '#### MENU ####' \
           '\n1 - Cerveja' \
           '\n2 - Tira gosto' \
           '\n3 - Agua' \
           '\n0 - Sair' \

    conta = 0
    taxa = 0

    #processamento
    while True:
        print(menu)
        produtos = input('Produtos escolhidos: ')
        if produtos == '0':
            break
        else:
            if produtos[1] == 'Cerveja':
                conta == conta + int(produto[0]) * 8.00
            elif produtos[2] == 'Tira_gosto':
                conta == conta + int(produto[0]) * 29.00
            elif produtos[3] == 'Agua':
                conta == conta + int(produto[0]) * 2.00

    qte_de_pagantes = input('Quantidade de pagantes: ')
    taxa = (conta / 100) * 10
    total = conta + taxa
    valor_pagante = total / qte_de_pagantes

    #saida
    print('Conta: R$%.2f' % float(conta))
    print('Taxa: R$%.2f' % float(taxa))
    print('Total: R$%.2f' % float(total))
    print('Valor do pagante: R$' % float(valor_pagante))



if __name__ == '__main__':
    main()



