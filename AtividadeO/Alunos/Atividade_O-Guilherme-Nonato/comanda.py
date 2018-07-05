def main():
    taxa_servico = 0.1
    preco_cerveja = 8
    preco_tira_gosto = 29
    preco_agua = 2
    valor_conta = 0
    pagantes = 1

    while True:
        menu()
        print()

        opcao = input()
        print()

        if opcao == 'a':
            quantidade, produto = input("Produto: ").split()
            print()
            quantidade = int(quantidade)

            if produto == 'C':
                valor_conta += preco_cerveja*quantidade

            elif produto == 'T':
                valor_conta += preco_tira_gosto*quantidade

            elif produto == 'A':
                valor_conta += preco_agua*quantidade

            else:
                print("Erro: produto inválido")
                print()

        elif opcao == 'b':
            pagantes = int(input("Quantidade de pagantes: "))
            print()

        elif opcao == 'c':
            valor_taxa = valor_conta*taxa_servico
            total = valor_conta + valor_taxa

        elif opcao == 'd':
            print("Valor da conta: R$ %.2f" % (valor_conta))
            print("Valor da taxa de serviço (10%%): R$ %.2f" % (valor_taxa))
            print("Valor total: R$ %.2f" % (total))
            print("Valor por pagante: R$ %.2f" % (total/pagantes))
            print()

        elif opcao == 'e':
            valor_conta = 0
            pagantes = 1

            print("Pagamento confirmado")
            print()

        else:
            print("Erro: opção inválida")
            print()


def menu():
    texto_menu = "a - Inserir produtos\n" \
                 "b - Definir quantidade de pagantes\n" \
                 "c - Calcular a conta\n" \
                 "d - Imprimir a conta\n" \
                 "e - Confirmar pagamento"

    print(texto_menu)


if __name__ == "__main__":
    main()
