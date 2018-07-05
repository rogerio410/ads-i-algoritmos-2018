def main():
    #entrada
    n1 = 1
    nc = int(input('Quantidade C: '))
    ntg = int(input('Quantidade Tg: '))
    na = int(input('Quantidade A: '))
    #calculos #saida
    while n1 != 0:
        n = int(input('Numero de pagantes: '))
        perc = 0.10
        valorconta = (nc * 8) + (ntg * 29) + (na * 2)
        taxaserv = valorconta * perc
        total = taxaserv + valorconta
        valorpagante = valorconta / n

        print('O valor da conta foi {}'.format(valorconta))
        print('O valor da taxa de serviço foi: {}'.format(taxaserv))
        print('O valor total foi {}'.format(total))
        print('O valor por pagante foi {}'.format(valorpagante))
        print('Confirmar o pagamento 0-sim 1-nao')
        confirmarpag = input()
        if confirmarpag == 0:
            novovalor = 0
            print('A conta foi zerada')
        else:
            print('A conta nao foi zerada')





if __name__ =='__main__':
    main()