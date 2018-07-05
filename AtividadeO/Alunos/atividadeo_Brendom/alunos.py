def main():
    cont_aprovados = 0
    cont_prova_final = 0
    cont_reprovados = 0
    aprovado = 0
    provafinal = 0
    reprovados = 0

    soma_medias = 0
    i = 0
    # entrada
    n = int(input())
    # trabalho
    for i in range(n):
        nome = input()
        n1 = float(input())
        n2 = float(input())
        n3 = float(input())

        media = (n1 + n2 + n3) / 3

        if media >= 7:
            aprovado = 1
        if 7 > media >= 4:
            provafinal = 1
        if media < 4:
            reprovados = 1
        cont_aprovados += aprovado
        cont_prova_final += provafinal
        cont_reprovados += reprovados
        # saida media aluno
        soma_medias += media
        print(nome, "media: %.1f" % media)

    media_classe = soma_medias / i

    # saida dados gerais da turma
    print("media da classe %.1f" % media_classe)
    print("numero de aprovados", cont_aprovados)
    print("numero de reprovados", cont_reprovados)
    print("em prova final", cont_prova_final)


if __name__ == '__main__':
    main()
