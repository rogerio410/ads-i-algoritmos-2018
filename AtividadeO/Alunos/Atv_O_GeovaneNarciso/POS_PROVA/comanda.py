def main():
    # entrada, processamento
    while True:
        opcao = menu()
        if opcao == 1:
            consumo = insere_produto()
        elif opcao == 2:
            pagantes = quant_pagantes()
        elif opcao == 3:
            calcular_conta(consumo, pagantes)
        elif opcao == 4:
            imprimir_conta(calcular_conta(consumo, pagantes))
        elif opcao == 5:
            print("\nPagamento confirmado.")
            break


def menu():
    print("\n##### COMANDA #####")
    print("(1) Inserir produtos")
    print("(2) Quantidade de pagantes")
    print("(3) Calcular conta")
    print("(4) Imprimir conta")
    print("(5) Confirmar pagamento")
    opcao = int(input("Informe uma opção:"))

    return opcao


def insere_produto():
    consumido = 0
    while True:
        quant, produto = input("\nInforme quantidade e o produto (C, TG ou A) (E E - Encerra):").upper().split()
        if produto == 'C':
            consumido += int(quant) * 8
        elif produto == 'TG':
            consumido += int(quant) * 29
        elif produto == 'A':
            consumido += int(quant) * 2
        elif produto == 'E':
            break

    return consumido


def quant_pagantes():
    quant_pagantes = int(input("\nInforme a quantidade de pagantes na mesa:"))

    return quant_pagantes


def calcular_conta(consumo, pagantes):
    c_consumo = consumo
    c_taxa = consumo * 0.1
    c_conta = consumo + consumo * 0.1
    c_valor_por_um = c_conta / pagantes
    calculo = [c_consumo, c_taxa, c_conta, c_valor_por_um]

    return calculo


def imprimir_conta(calculo):
    print("\nValor da conta: R$ {:.2f} reais." .format(calculo[0]))
    print("Valor da taxa: R$ {:.2f} reais." .format(calculo[1]))
    print("Valor total com a taxa: R$ {:.2f} reais." .format(calculo[2]))
    print("Valor por pagante: R$ {:.2f} reais." .format(calculo[3]))


if __name__ == '__main__':
    main()
