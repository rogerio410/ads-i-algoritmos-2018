def main():
    # arquivo = open(arquivo, encoding="ISO-8859-1")
    arquivo = open(arquivo)

    registros = []
    for linha in arquivo.readlines():
        registros.append(linha.strip().split(';'))

    print(registros)
if __name__=='__main__':
    main()