def main():
    financiamento = 80000
    parcela = 1200
    cont_meses = 0
    pagamento = 0
    juro = 0
    valor_devedor = 0
    while pagamento < 80000:
        pagamento += parcela
        valor_devedor = financiamento - pagamento
        valor_devedor = valor_devedor + juro
        juro = (valor_devedor * 0.65) / 100
        parcela = parcela
        cont_meses += 1

    print('ultima parcela paga: R$ %.2f' % float(parcela + valor_devedor))
    print('Quantidade de meses :', cont_meses)


if __name__ == '__main__':
    main()
