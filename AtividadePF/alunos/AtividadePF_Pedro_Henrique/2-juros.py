def main():
    valor_do_emprestimo = 80000
    meses = 0

    while (valor_do_emprestimo - 1200) > 0:
        valor_do_emprestimo += (valor_do_emprestimo * (0.65 / 100))
        valor_do_emprestimo -= 1200
        meses += 1

    meses += 1

    print('O tempo para finalizar o pagamento de todas as parcelas será de %d meses' % meses)
    print('O ultimo pagamento vai ser no valor de % .2f ' % valor_do_emprestimo)


if __name__ == '__main__':
    main()
