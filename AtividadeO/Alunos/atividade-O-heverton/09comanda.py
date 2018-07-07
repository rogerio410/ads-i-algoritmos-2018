"""
09comanda.py
"""


def main():
    print('COMANDA ')
    print('- - - - - - - - - -  - - - - - - - -')
    print('Cerveja 8,00 reais - 1C')
    print('Tira-Gosto 29,00 reais - 1T')
    print('Agua 2,00 - 1A\n')

    conta = 0
    taxa = 0

    while True:

        inserir_produtos = input('Insira os produtos: (0 para sair da inserção) ')
        if inserir_produtos == '0':
            break
        else:
            if inserir_produtos[1] == 'C':
                conta += int(inserir_produtos[0]) * 8
            elif inserir_produtos[1] == 'T':
                conta += int(inserir_produtos[0]) * 29
            elif inserir_produtos[1] == 'A':
                conta += int(inserir_produtos[0]) * 2


    qtde_de_pagantes = input("\nQtde de pagantes na mesa: ")
    taxa_de_servico = (conta / 100) * 10
    conta_total = conta + taxa_de_servico
    per_capta = conta_total / int(qtde_de_pagantes)

    print('\nValor da conta: R$ %.2f' % float(conta))
    print('Valor da taxa de serviço: R$ %.2f' % float(taxa_de_servico))
    print('Valor total + taxa de serviço: R$ %.2f' % float(conta_total))
    print('Valor por pagante: para cada uma dos '+ str(qtde_de_pagantes) + ' pagantes fica o valor R$ ' + str(per_capta))


    
if __name__ == '__main__':
    main()
