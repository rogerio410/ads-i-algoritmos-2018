def main():
    n = int(input("Numero de alunos: "))
    total_aluno = int(n)
    pontos_class = 0
    cont_aprovados = 0
    cont_alunos_prova_final = 0
    cont_alunos_reprovado = 0
    while n > 0:
        nome, n1, n2, n3 = input().split()
        media = (float(n1) + float(n2) + float(n3)) / 3
        if media >= 7:
            cont_aprovados += 1
        elif media < 7 and media > 4:
            cont_alunos_prova_final += 1
        elif media < 4:
            cont_alunos_reprovado += 1

        print("Media aritmética: %.2f" % media)
        pontos_class += float(n1) + float(n2) + float(n3)
        n -= 1
    # print("Media da classe: %.2f" % float(pontos_class)/total_aluno)
    print("Quantidade de alunos aprovados: {}".format(cont_aprovados))
    print("Quantidade de alunos em prova final: {}".format(cont_alunos_prova_final))
    print("Quantidade de alunos reprovados: {}".format(cont_alunos_reprovado))
    media_da_classe = pontos_class / total_aluno
    print("Media da classe: %.2f" % media_da_classe)



if __name__ == '__main__':
    main()