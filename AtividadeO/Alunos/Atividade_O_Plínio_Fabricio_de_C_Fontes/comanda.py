def main():
    produtos = input('C para cerveja, T, para tiragosto e A, para água. Para encerrar, digite 0 0')
    produtos = produtos.split()
    conta = 0.0
    while produtos != '0 0':
        quantidade = int(produtos[0])
        mercadoria = produtos[1]
        if mercadoria == 'C':
            conta += quantidade * 8.00
        elif mercadoria == 'T':
            conta += quantidade * 29.00
        elif mercadoria == 'A':
            conta += quantidade * 2.00
    pagantes = int(input('quantos pagantes?\n'))
    conta_com_10_por_cento = conta + (0.1 * conta)
    print('Conta: R$', conta)
    print('Taxa de Serviço: R$', conta * .10)
    print('Conta total: R$', conta_com_10_por_cento)
    print('Valor por pagante: R$', conta_com_10_por_cento / pagantes)
    print('confirmar pagamento: digite 0 0')

if __name__=='__main__':
    main()



