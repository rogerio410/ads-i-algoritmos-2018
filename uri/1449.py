def main():
    casos_teste = int(input())

    for c in range(casos_teste):
        valores = input().split()
        quant_palavras, quant_linhas = int(valores[0]), int(valores[1])
        lista_traducao = traduzindo(quant_linhas, quant_palavras)
        
        for p in range(quant_linhas):
            frase_print = ' '.join(lista_traducao[p])
            print(frase_print)
        print()


def obtendo_tudo(quant_linhas, quant_palavras):
    lista_jap = [''] * quant_palavras
    lista_br = [''] * quant_palavras
    lista_musc = [''] * quant_linhas

    for p in range(quant_palavras):
        lista_jap[p] = input()
        lista_br[p] = input()
    
    for p in range(quant_linhas):
        lista_musc[p] = input().split()
    
    return lista_jap, lista_br, lista_musc


def traduzindo(quant_linhas, quant_palavras):
    lista_jap, lista_br, lista_musc = obtendo_tudo(quant_linhas, quant_palavras)
    lista_traducao = lista_musc[:]

    for pc in range(quant_linhas): # linhas
        for pv in range(len(lista_musc[pc])): # palavras da linha
            palavra = lista_musc[pc][pv]
            for pp in range(len(lista_jap)): # dicionario
                if palavra == lista_jap[pp]:
                    lista_traducao[pc][pv] = lista_br[pp]
    
    return lista_traducao


if __name__ == '__main__':
    main()
