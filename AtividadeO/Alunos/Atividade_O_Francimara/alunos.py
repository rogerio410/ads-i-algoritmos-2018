def main():
    # entrada
    total_de_alunos = int(input('Digite o numero de alunos: '))
    media_de_todos_alunos = 0
    alunos_aprovados = 0
    alunos_pf = 0
    alunos_reprovados = 0

    # processamento
    for i in range(total_de_alunos):
        n1 = float(input("Digite a primeira nota do aluno: "))
        n2 = float(input("Digite a segunda nota do aluno: "))
        n3 = float(input("Digite a terceira nota do aluno: "))
        media_aritmetica = (n1 + n2 + n3) / 3
        print(media_aritmetica)

        media_de_todos_alunos = media_aritmetica + 1

        if media_aritmetica >= 7:
            alunos_aprovados = alunos_aprovados + 1
        elif media_aritmetica >= 4:
            alunos_pf = alunos_pf + 1
        else:
            alunos_reprovados = alunos_reprovados + 1

    #saida
    print('A media de todos os alunos eh {}'.format(media_de_todos_alunos))
    print('Quantidade de alunos aprovados eh {}'.format(alunos_aprovados))
    print('Quantidade de alunos em prova final eh {}'.format(alunos_pf))
    print('Quantidade de alunos reprovados eh {}'.format(alunos_reprovados))


if __name__ == '__main__':
    main()

