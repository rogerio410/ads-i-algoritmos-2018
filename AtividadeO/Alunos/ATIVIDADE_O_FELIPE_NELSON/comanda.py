def main():
    
    conta = 0
    print('****MENU****\n')
    quantidade, comida = input('a- Inserir produto\nDigite o número de comidas e a letra da comida:'
                               '\nCerveja(C)- 8 reais\nTira Gosto(T)- 29 reais\nÁgua(A)- 2 reais\n').split()
    if comida == 'C':
        conta += 8 * int(quantidade)
    elif comida == 'T':
        conta += 29 * int(quantidade)
    elif comida == 'A':
        conta += 2 * int(quantidade)
    q_pagantes = int(input('b- Definir quantidade de pagantes\nDigite o número de pagantes:\n'))
    print('c- Calcular a conta. Com taxa de 10%')
    taxa = conta * 0.1
    calcular_conta = conta + taxa
    print('d- Imprimir a conta\n'
          'I- valor da conta: R$ %.2f\n'
          'II- valor da taxa de serviço: R$ %.2f\n'
          'III- valor totao com taxa: R$ %.2f\n'
          'IV- valor por pagante: R$ %.2f' % (conta, taxa, calcular_conta, calcular_conta/q_pagantes))
    print('e- Confirmar pagamento')


if __name__ == '__main__':
    main()
