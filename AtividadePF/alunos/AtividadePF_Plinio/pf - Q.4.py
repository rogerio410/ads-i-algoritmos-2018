def main():
    capital = 80000
    juros = .0065
    pagamento_mensal = 1200
    meses = 0
    while capital > 1200:
        meses += 1
        juros = 0.0065 * capital
        capital += juros
        capital -= 1200
    print(meses +1,'meses')
    print('parcela final {:.2f}'.format(capital))


if __name__=='__main__':
    main()