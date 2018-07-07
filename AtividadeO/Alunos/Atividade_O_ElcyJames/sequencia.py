def main():
    if adicao_ed(1) == adicao_de(1) == separa_ed(1) == separa_de(1):
        print('São iguais')
        print(adicao_ed(1), adicao_de(1), separa_ed(1), separa_de(1))
    else:
        print('São diferentes')
        print(adicao_ed(1), adicao_de(1), separa_ed(1), separa_de(1))

def adicao_ed(soma):
    for i in range(2, 10001):
        if i % 2 == 0:
          soma -= 1/i
        else:
            soma += 1/i
    return soma

def adicao_de(soma):
    for i in range(10000, 1, -1):
        if i % 2 == 0:
          soma -= 1/i
        else:
            soma += 1/i
    return soma

def separa_ed(soma):
    for i in range(2, 10001):
        if i % 2 == 0:
            soma -= 1/i
    for i in range(2, 10001):
        if i % 2 != 0:
            soma += 1 / i
    return soma

def separa_de(soma):
    for i in range(10000, 1, -1):
        if i % 2 == 0:
            soma -= 1/i
    for i in range(10000, 1, -1):
        if i % 2 != 0:
            soma += 1 / i
    return soma


if __name__ == '__main__':
    main()




