def main():
    financiamento = 80000
    juros = 0.65
    parcela = 1200

    soma = 0
    for i in range(financiamento):
        soma += 1
        parcela = parcela * juros

    print(soma)
    print(parcela)


if __name__ == '__main__':
    main()