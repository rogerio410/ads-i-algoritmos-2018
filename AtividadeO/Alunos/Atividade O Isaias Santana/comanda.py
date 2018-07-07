def main():
    cont_c = 0
    cont_a = 0
    cont_t = 0
    while True:
        opcao = int(input("1 - Inserir produtos\nOpção: "))
        if opcao == 1:
            while True:
                quantidade, produto = input("Informe a quantidade e o produto(Ex: 2 C): ").split()
                if produto == "c":
                    cont_c += 1
                elif produto == "a":
                    cont_a += 1
                elif produto == "t":
                    cont_t += 1
                print("### Obs: Digite (0 0) para informar a quantidade de pagantes")
                if int(quantidade) == 0 and int(produto) ==  0:
                    quantidade_pagantes = int(input("Quantidade de pagantes: "))
                    valor_conta = cont_c*8 + cont_t*29 + cont_a*2
                    taxa_servico = (10/100)*valor_conta
                    valor_total = valor_conta + taxa_servico
                    valor_pagante = valor_total/quantidade_pagantes
                    print("Conta: R$ %.2f" % valor_conta)
                    print("Taxa de servico: R$ %.2f" % taxa_servico)
                    print("Valor total: R$ %.2f" % valor_total)
                    print("Valor por pagante: R$ %.2f" % valor_pagante)
                    opcao = int(input("1 - Confirmar pagamento ?: "))
                    if opcao == 1:
                        break


if __name__ == '__main__':
    main()