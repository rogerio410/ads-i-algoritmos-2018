def main():
    #entrada
    operacao = menu()
    conta = 0
    pagantes = 1
    #processamento()
    while operacao != "e" :
        if operacao == "a":
            conta = adicionar_produtos(conta)
        elif operacao == "b":
            pagantes = def_quant_pagantes()
        elif operacao == "c":
            calcular_conta(conta)
        elif operacao == "d":
            imprimir_conta(conta,pagantes)

        operacao = menu()

def menu():
    operacao = input("""Com o que posso ajuda-lo?
    a - adicionar produtos
    b - definir a quantidade de pagantes
    c - calcular a conta
    d - imprimir conta
    e - confirmar pagamento
    """)
    if operacao == "e":
        print("Pagamento Confimado!\n Obrigado e volte sempre!")
    return operacao

def adicionar_produtos(conta):
    nova_conta = conta
    produto_adicionado = input("qual a quantidade de produto a ser adicionada? A = agua, C = cerveja, T = Tira Gosto Ex= 3 A -> 3 águas ")
    tipo = produto_adicionado.split()[1]
    quantidade = int(produto_adicionado.split()[0])
    if tipo == "A":
        nova_conta += quantidade*2
    elif tipo == "C":
        nova_conta += quantidade*8
    elif tipo == "T":
        nova_conta += quantidade*29

    return nova_conta

def def_quant_pagantes():
    pagantes = int(input("Digite a quantidade de pagantes da conta"))

    return pagantes

def calcular_conta(conta):

    print("o total a ser pago é :{:.2f}".format(conta*1.1))

def imprimir_conta(conta,pagantes):
    print("Valor da Conta: {:.2f}\n Valor da Taxa de Serviço: {:.2f}\n Valor Total da Conta: {:.2f}\n Valor por Pagante: {:.2f}".format(conta,conta*0.1,conta*1.1,(conta*1.1)/pagantes))



if __name__ == '__main__':
    main()
