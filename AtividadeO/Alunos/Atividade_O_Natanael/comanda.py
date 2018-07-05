# função para calcular o preco dos produtos
def calcular_preco():
    # entradas
    produto, quantidade = input('Digite o codigo do produto(C-cerveja, T-tira gosto e A-agua) seguida da quantidade:')\
        .split()

    # variavel que terá o preco
    preco = 0

    # processamento
    if produto == 'C' or produto == 'c':
        preco = int(quantidade) * 8
    elif produto == 'T' or produto == 't':
        preco = int(quantidade) * 29
    elif produto == 'A' or produto == 'a':
        preco = int(quantidade) * 2

    # retorno(saida)
    return preco

# função que define a quantidade de pessoas pagantes
def quantidade_pagantes():
    # entrada
    pessoas_pagantes = int(input('Digite a quantidade de pessaos pagantes:'))

    # retorno
    return pessoas_pagantes


# função principal
def main():
    # menu
    menu = '*****Valor da comanda*****' \
           '\n1-Inserir produtos:Cerveja(8 reais), Tira Gosto(29 reias),' \
           '\nAgua(2 reais)' \
           '\n2-Definir quantidade de Pagantes na mesa' \
           '\n3-Calcular a conta,incluindo 10% de taxa de serviço' \
           '\n4-Imprimir Conta' \
           '\n5-Confirmar pagamento'

    # contadores
    saldo = 0
    quant_pessoas_pagantes = 0
    conta = 0

    # processamento
    while True:
        # entrasa
        opcao = int(input(menu))
        if opcao == 1:
            saldo += calcular_preco()
        elif opcao == 2:
            quant_pessoas_pagantes = quantidade_pagantes()
        elif opcao == 3:
            if saldo == 0:
                # saida caso a pessoa peça para calcular os 10% sem ter pedido nada
                print('Ainda não foi pedido nenhum produto!')
            else:
                conta = saldo + saldo * 0.10
        elif opcao == 4:
            # saida da opção 4
            print('Conta:')
            print('\tValor da conta->%d' % saldo)
            print('\tValor da taxa de serviço-.%.2f' % (saldo * 0.10))
            print('\tValor Total com a taxa de serviço->%.2f' % conta)
            if quant_pessoas_pagantes == 0:
                print('\tValor por pagante->%.2f' % (conta / 1))
            else:
                print('\tValor por pagante->%.2f' % (conta / quant_pessoas_pagantes))
        elif opcao == 5:
            saldo = 0
            quant_pessoas_pagantes = 0
            conta = 0


if __name__ == '__main__':
    main()
