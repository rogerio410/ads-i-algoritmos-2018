def main():

        print('MENU:')
        print('a - Inserir Produtos')
        print('b - Dedinir uma quantidade de pagantes na mesa')
        print('c - Calcular a conta total')
        print('d - Imprimir a conta')
        print('e - Confirmar pagamento')
        opcao = str(input('Selecione uma opção: ')).upper()


            if opcao == 'A':

                pedidos = int(input('Digite a quantidade de pedidos que deseja fazer: '))
                print('C - Cerveja / T - Tira gosto / A - Água')

                for i in range(1, pedidos + 1):

                    produtos = input('Insira a quantidade e o produto: ')
                    produtos.split()
                    a = int(produtos[0])
                    b = str(produtos[1])

            elif opcao == 'B':
                quantidade_de_pagantes = int(input('Defina uma quantidade de pagantes na mesa: '))


if __name__ == '__main__':
    main()