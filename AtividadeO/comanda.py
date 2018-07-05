def main():

    menu = '**** COMANDA *****\n' \
           '1 - inserir produto\n' \
           '2 - qtd pagantes\n' \
           '3 - calcular conta\n' \
           '4 - pagar conta\n' \
           '0 - sair\n\n'

    opcao = int(input(menu))

    valor_conta = 0.0
    qtd_pagantes = 1

    while opcao != 0:

        if opcao == 1:
            valor_conta += novo_produto()
        elif opcao == 2:
            qtd_pagantes = int(input('Quantos? '))
        elif opcao == 3:
            taxa_servicos = valor_conta * 0.1
            valor_final = valor_conta + taxa_servicos
            por_pagante = valor_final / qtd_pagantes
            print('Valor Conta : R$ %.2f' % valor_conta)
            print('Taxa de Serv: R$ %.2f' % taxa_servicos)
            print('Valor Final : R$ %.2f' % valor_final)
            print('Valor p/ Pag: R$ %.2f' % por_pagante)
            print('Dinheiro ou Cartão...')
        elif opcao == 4:
            valor_conta = 0
            valor_final = 0.0
            qtd_pagantes = 1
            print('Conta paga com sucesso!!\n')
            print('Seu retorno é a nossa recompensa!')
        else:
            print('Opcao invalida!!\n')

        opcao = int(input(menu))


def novo_produto():

    entrada = input('Item: ')
    dados = entrada.split()

    qtd = int(dados[0])
    cod = dados[1]

    if cod == 'C':
        valor_do_item = 8.0 * qtd
    elif cod == 'T':
        valor_do_item = 29.0 * qtd
    elif cod == 'A':
        valor_do_item = 2.0 * qtd
    else:
        valor_do_item = 0.0

    return valor_do_item


if __name__ == '__main__':
    main()