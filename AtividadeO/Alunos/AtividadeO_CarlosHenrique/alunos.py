def main():
    num_alunos = int(input())
    situacao_classe(num_alunos)


def situacao_classe(num):
    i = 0
    aprovado = 0
    reprovado = 0
    prova_final = 0
    media_classe = 0

    while i < num:
        nome = input()
        nota1 = float(input())
        nota2 = float(input())
        nota3 = float(input())

        media_aluno = (nota1 + nota2 + nota3) / 3

        if media_aluno >= 7:
            aprovado += 1
        elif media_aluno > 4:
            prova_final += 1
        elif media_aluno < 4:
            reprovado += 1

        media_classe += media_aluno
        i = 1 + 1

    media_classe = media_aluno / num
    i = 1 + 1

    print("Media da Classe = %.2f" % media_classe)
    print("quantidade de alunos aprovados: %d" % aprovado)
    print("quantidade de alunos reprovados: %d" % reprovado)
    print("quantidade de alunos de prova final: %d" % prova_final)


if __name__ == '__main__':
    main()