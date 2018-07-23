def main():
    t = int(input())

    for i in range(t):
        qtd_verbetes, qtd_linhas = list(map(int, input().split()))
        verbetes = [None] * qtd_verbetes
        linhas = [None] * qtd_linhas

        preencher_dicionario(verbetes, qtd_verbetes)
        receber_linhas(linhas, qtd_linhas)

        for j in range(qtd_linhas):
            traduzida = traduzir_linha(linhas[j], verbetes)
            print(traduzida)
        print()


def preencher_dicionario(verbetes, qtd_verbetes):
    """Vetor bi-dimensional para guardar o par de traducoes: [[jap1][br1], [jap2][br2]]"""
    for i in range(qtd_verbetes):
        jap = input()
        br = input()
        verbetes[i] = [jap, br]


def receber_linhas(linhas, qtd_linhas):
    for i in range(qtd_linhas):
        linhas[i] = input()


def traduzir_linha(linha, verbetes):
    palavras_traduzidas = linha.split()

    for i in range(len(palavras_traduzidas)):
        palavra = palavras_traduzidas[i]
        palavras_traduzidas[i] = traduzir_palavra(palavra, verbetes)

    return ' '.join(palavras_traduzidas)


def traduzir_palavra(palavra, verbetes):
    traducao = palavra
    for i in range(len(verbetes)):
        if palavra == verbetes[i][0]: # pos 0 -> Jap
            return verbetes[i][1]     # pos 1 -> Br
    return traducao


if __name__ == '__main__':
    main()