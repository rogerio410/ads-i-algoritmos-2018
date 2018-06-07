def main():
    # python3 Fabio03_q23.py < fb03_q23.txt
    while True:
        try:
            programa()
        except:
            break


def programa():
    n = int(input())

    for i in range(n):
        funcionario = input()
        dados = funcionario.split()
        codigo = dados[0]
        horas = int(dados[1])
        dependentes = int(dados[2])

        salario_bruto = horas*12 + dependentes*40
        inss = salario_bruto * 0.085
        ir = salario_bruto * 0.05

        salario_liquido = salario_bruto - inss - ir
        print('Func:', codigo)
        print('\tINSS:',"%.2f" % inss)
        print('\tIR:', "%.2f" % ir)
        print('\tSalário Líquido:', "%.2f" % salario_liquido)



if __name__ == '__main__':
    main()