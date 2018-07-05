def main():
    total = 0
    total_invertido = 0
    total_ed = 0
    total_de = 0
    operacao = True
    for i in range(1,10000):
        if operacao:
            total += 1/i
        else:
            total -= 1/i
        total_ed += 1/i
        operacao = not operacao
    operacao = False
    for i in range(10000,0,-1):
        if operacao:
            total_invertido += 1/i
        else:
            total_invertido -= 1/i
        operacao = not operacao
        total_de += 1/i


    print("a)",total_ed)
    print("b)",total_de)
    print("c)",total)
    print("d)",total_invertido)

def soma(n, n1):
    return  n + n1


def subtrai(n, n1):
    return  n - n1


if __name__ == "__main__":
    main()
