def main():
    # Entrada
    n = int(input("Número de alunos: "))
    print()

    # Processamento
    aprovados = 0
    prova_final = 0
    reprovados = 0
    soma_medias = 0

    for i in range(n):
        entrada = input("Nome e notas: ").split()

        n1 = float(entrada[1])
        n2 = float(entrada[2])
        n3 = float(entrada[3])

        media = (n1+n2+n3) / 3

        soma_medias += media

        if media >= 7:
            aprovados += 1

        elif media >= 4:
            prova_final += 1

        else:
            reprovados += 1

    print()

    media_turma = soma_medias/n

    # Saída
    print("%d aluno(s) aprovado(s)" % (aprovados))
    print("%d aluno(s) de prova final" % (prova_final))
    print("%d aluno(s) reprovado(s)" % (reprovados))
    print("Média da turma: %.2f" % (media_turma))


if __name__ == "__main__":
    main()
