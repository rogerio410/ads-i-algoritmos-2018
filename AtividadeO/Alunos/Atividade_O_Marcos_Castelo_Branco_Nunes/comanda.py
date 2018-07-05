def main():
    menu()
    opcao = input()
    total = 0
    total_c_taxa = 0
    total_pagante = 0
    pagantes = 0
    while opcao != 0:
        if opcao == "1":
            qnt, prod = input("Digite a quantidade e o codigo do pedido").split()
            qnt = int(qnt)

            preco = CalculaProduto(prod,qnt)
            total += preco
            print("Pedido inserido com sucesso!\n")
            menu()

        elif opcao == "2":
            pagantes = int(input("Digite o numero de pagantes"))
            print("Pagantes Inseridos com sucesso!")
            menu()

        elif opcao == "3":
            print("Total:",total)
            print("Valor da taxa: 10%")
            total += CalculaTaxa(total,10)
            print("Valor com taxa:",total)
            print("Valor por pagante:", total / pagantes)
            menu()

        elif opcao == "4":
            confirmar = "n"
            while confirmar != "y":
                print("Confirmar pagamento(y/n): ")
                confirmar = input()
            total = 0
            menu()

        else:
            print("Insira uma opcao válida!")
            menu()
        opcao = input()

def CalculaProduto(produto, qntd):
    if produto == "C":
        return qntd * 8
    elif produto == "T":
        return qntd * 29
    elif produto == "A":
        return  qntd * 2


def CalculaTaxa(valor,taxa):
    return (taxa/100) * valor


def menu():
    print("===============================================")
    print("Digite o valor de acordo com a ação requerida.")
    print("1 - Inserir Produtos na conta.")
    print("2 - Definir quantidade de pagantes.")
    print("3 - Imprimir Conta.")
    print("4 - Confirmar Pagamento")
    print("0 - Sair")

if __name__ == '__main__':
    main()
