# https://www.urionlinejudge.com.br/judge/pt/problems/view/1257


def main():
    qtd_teste = int(input())

    for i in range(qtd_teste):
        hash_teste = 0  # a cada teste zera o hash
        qtd_linhas = int(input())
        for j in range(qtd_linhas):
            linha = input()
            hash_teste += hash_linha(j, linha)
        print(hash_teste)


def hash_linha(pos: int, linha: str) -> int:
    valor = 0
    for i in range(len(linha)):
        letra = linha[i]
        posicao_alfabeto = ord(letra) - 65  # Alfabeto começa em 65 na tabela ASCII
        valor += pos + i + posicao_alfabeto

    return valor


if __name__ == '__main__':
    main()
