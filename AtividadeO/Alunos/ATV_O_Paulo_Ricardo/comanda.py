def main():

    while True:

        cerveja = 0
        tira_gosto = 0
        agua = 0

        for produtos in range(3):
            produto = input('Digite produto: ').split(' ')

            if produto[1] == 'C':
                cerveja = int(produto[0])
            elif produto[1] == 'A':
                agua = int(produto[0])
            else:
                tira_gosto = int(produto[0])

        pagantes = int(input('Quantidade de pagantes: '))

        valor_conta = cerveja * 8 + tira_gosto * 29 + agua * 2
        valor_taxa = valor_conta * 0.10
        valor_total_conta = valor_conta + valor_taxa
        valor_por_pagante = valor_total_conta / pagantes

        print('Valor da conta {:.2f} reais'.format(valor_conta))
        print('Valor da taxa {:.2f} rais'.format(valor_taxa))
        print('Valor total da conta {:.2f} reais'.format(valor_total_conta))
        print('Valor por pagante {:.2f} reais'.format(valor_por_pagante))

        confirmacao = input('"S" para pagamento efetudado, "N" para pagamento nao efetuado: ')

        if confirmacao == 'N':
            break


if __name__ == '__main__':
    main()
