def main():
    conta = 0
    while True:
        menu = '######## MENU ###########' \
               '1 - quantos pagantes: ' \
               '2 - pedidos: ' \
               '3 - calcular conta' \
               '4 - imprimir conta' \
               '5 - confirmar pagamento' \
               '6 - SAIR'
        opc = input('opcao: ' )
        if opc == '1':
            quant_pag = pagantes()

        elif opc == '2':
            conta  = pedidos(conta)

        elif opc == '3':
            calc(conta, quant_pag)
        elif opc == '4':
            imprimir()
        elif opc == '5':
            confirm()
        else:
            break


def pagantes():
    pagant = input('quantos pagantes: ')
    return pagant

def pedidos(conta):
    pedi = input('pedidos: ')
    mesa  = pedi.split()
    if mesa[1] == 'C':
        valor = int(mesa[0]*8)
    elif mesa[1] == 'A':
        valor = int(mesa[0] * 2)
    elif mesa[1] == 'T':
        valor = int(mesa[0] * 29)

    conta = conta + valor
    return conta

def calc(conta, quant_pag):
    serv = conta/10
    print('Total da conta {}. Valor do servico {} . '.format(conta,serv))
    print('Total da conta {}. Valor por pagante {}'.format(conta+serv, (conta/quant_pag)))



if __name__ == '__main__':
    main()

