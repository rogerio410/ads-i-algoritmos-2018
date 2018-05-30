def main():
    ddd = int(input())
    cidade = obter_cidade(ddd)
    print(cidade)


def obter_cidade(ddd):
    if ddd == 61:
        cidade = 'Brasilia'
    elif ddd == 71:
        cidade = 'Salvador'
    elif ddd == 11:
        cidade = 'Sao Paulo'
    elif ddd == 21:
        cidade = 'Rio de Janeiro'
    elif ddd == 32:
        cidade = 'Juiz de Fora'
    elif ddd == 19:
        cidade = 'Campinas'
    elif ddd == 27:
        cidade = 'Vitoria'
    elif ddd == 31:
        cidade = 'Belo Horizonte'
    else:
        cidade = 'DDD nao cadastrado'

    return cidade


if __name__ == '__main__':
    main()