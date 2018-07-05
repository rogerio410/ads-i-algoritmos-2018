def main():
    total = 0
    pagantes = 1
    valor_a_pagar = 0

    while True:
        opcao = menu()

        if opcao == 'a':
            total = inserir_produto(total)
        elif opcao == 'b':
            pagantes = total_de_pagantes()
        elif opcao == 'c':
            valor_a_pagar = calcular_conta(total, pagantes)
            print(valor_a_pagar)
        elif opcao == 'd':
            imprime_conta(total, valor_a_pagar, pagantes)
        elif opcao == 'e':
            print('Conta fechada')
            total = 0
            pagantes = 1
            valor_a_pagar = 0


def imprime_conta(total, valor, pagantes):
    valor_pagante = valor / pagantes

    print('Valor da conta igual a R$ %.2f ' % total)
    print('taxa de servico igual a 10%%')
    print('Valor total com taxa igual a R$ %.2f' % valor)
    print('Valor por pagantes R$ %.2f' % valor_pagante)


def calcular_conta(total, pagantes):
    return total + (total * 0.1)


def total_de_pagantes():
    print('=================================')
    print('               total de pagantes')
    respota = int(input('Qual o total de pagantes: '))
    return respota


def inserir_produto(total):
    print('=================================')
    print('               inserir produto')
    print('C - Cerveja')
    print('T - Tira gosto')
    print('A - Agua')
    quantidade, escolha = input('>>> ').split()
    quantidade = int(quantidade)

    if escolha == 'C':
        total += 8 * quantidade
    elif escolha == 'T':
        total += 29 * quantidade
    else:
        total += 2 * quantidade

    return total


def menu():
    print('================================')
    print('                menu')
    print('a - inserir produtos')
    print('b - definir a quantidade de pagantes')
    print('c - calcular a conta')
    print('d - imprimir conta')
    print('e - confirmar pagamento')
    resposta = input('>>> ')

    return resposta


if __name__ == '__main__':
    main()
