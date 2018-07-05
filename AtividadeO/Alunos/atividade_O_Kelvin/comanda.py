def main():
    #entrada

    quantidade, produto = input('Inserir produto: ').split()
    pagantes = int(input('Digite a quantidade de pagantes: '))
    quantidade = int(quantidade)
    preco = 0

    #processamento
    if produto == 'C':
        preco = 8
    elif produto == "TG":
        preco = 29
    elif produto == 'A':
        preco = 2
    conta = preco * quantidade
    conta_com10_porcento = (preco * quantidade) * 1.1
    valor_da_taxa = conta_com10_porcento - conta
    valor_por_pagante = conta_com10_porcento / pagantes
    #saida
    print('======MENU======')
    print('Valor da conta: %.2f' %conta)
    print('Valor da taxa de serviço %.2f' %valor_da_taxa)
    print('Valor total com a taxa de serviço: %.2f' %conta_com10_porcento)
    print('Valor por pagante: %.2f ' %valor_por_pagante)

    pagamento = int(input('Informe o valor a ser pago: '))
    if pagamento == conta_com10_porcento:
        pass

if __name__ == '__main__':
    main()