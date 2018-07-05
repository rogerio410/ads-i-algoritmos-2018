def main():
    # entrada e processamento
    while True:
        print('~~~~~~~~~menu~~~~~~~~~')
        print('Cerveja (8 reais) = 1 C')
        print('Tira Gosto (29 reais) = 1 T')
        print('Agua (2 reais) = 1 A')
        print()
        conta = 0
        taxa = 0

        while True:
            inserir_produtos = input('Inserir produtos (digite 0 para fim): ')
            if inserir_produtos == '0':
                break
            else:
                if inserir_produtos[2] == 'C':
                    conta += int(inserir_produtos[0]) * 8
                if inserir_produtos[2] == 'T':
                    conta += int(inserir_produtos[0]) * 29
                if inserir_produtos[2] == 'A':
                    conta += int(inserir_produtos[0]) * 2
        pagantes = int(input('Definir Quantidade de Pagantes na mesa: '))
        taxa += (conta * 10) / 100

    # saida
        print('Conta = R$ {}'.format(conta))
        print('Valor da taxa de serviço = R$ {}'.format(taxa))
        print('Valor total com taxa de serviço = R$ {}'.format(conta + taxa))
        print('Valor do pagante = R$ {}'.format((conta+taxa)/pagantes))
        print()

        zerar_conta = int(input('Confirmar pagamento (digite 1): '))
        if zerar_conta != 1:
            break


if __name__ == '__main__':
    main()
