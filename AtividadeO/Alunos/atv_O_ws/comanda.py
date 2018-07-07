def main():
    menu = '''
    __________________________________________________
    [ 1 ] - Inserir produtos.
    [ 2 ] - Definir a quantidade de pagantes na mesa.
    [ 3 ] - Calcular conta.
    [ 4 ] - Imprimir conta.
    [ 5 ] - Confirmar pagamento.
    __________________________________________________\n'''
    total_conta = 0
    pessoas_mesa = 0
    while True:
        escolha = int(input(menu))
        if escolha == 1:
            while True:
                entrada = input('Digite a compra [ex.: 1 água - 1 A]\n[ A - água, C - Cerveja, T - Tira gosto, 0 - SAIR]\n').split()
                if entrada[0] == '0':
                    break
                elif entrada[1] == 'C':
                    total_conta += int(entrada[0]) * 8
                elif entrada[1] == 'A':
                    total_conta += int(entrada[0]) * 2
                elif entrada [1] == 'T':
                    total_conta += int(entrada[0]) * 29
                else:
                    break

        elif escolha == 2:
            pessoas_mesa = int(input('Digite a quantidade de pessoas na mesa: '))

        elif escolha == 3:
            taxa = total_conta * 0.10
            print('Total: R${:.2f}'.format(total_conta + taxa))
        elif escolha == 4:
            taxa = total_conta*0.10
            total = total_conta + taxa
            print('O total parcial: R${:.2f}'.format(total_conta))
            print('Taxa de serviço: R${:.2f}'.format(taxa))
            print('Total final: R${:.2f}'.format(total))
            print('Por {} pessoa(s): R${:.2f}'.format(pessoas_mesa, total/pessoas_mesa ))
        elif escolha == 5:
            total_conta = 0


if __name__ == '__main__':
    main()
